from overflow_logic import get_overflow_list, overflow
from custom_data_structures import Queue


def copy_board(board):
    return [row.copy() for row in board]


def evaluate_board(board, player):
    player_gem_count = opponent_gem_count = total_gem_count = board_value = 0
    opponent = -player

    for row_idx in range(len(board)):
        for col_idx in range(len(board[row_idx])):
            cell = board[row_idx][col_idx]
            total_gem_count += abs(cell)

            if cell != 0:
                if (abs(cell) / cell) == player:
                    player_gem_count += abs(cell)
                elif (abs(cell) / cell) == opponent:
                    opponent_gem_count += abs(cell)

                if (row_idx in {2, 3}) and (col_idx in {2, 3}):
                    board_value += 1 if (abs(cell) / cell) == player else -1

    if total_gem_count == 0:
        return 0

    gem_score = player_gem_count / total_gem_count
    score = gem_score + board_value * 0.015
    return round(score, 1)


class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height=4):
            self.board_state = board
            self.depth_level = depth
            self.player = player
            self.tree_height = tree_height
            self.previous_move = None
            self.child_nodes = []
            self.node_score = None
            self.best_move = None

        def get_valid_moves(self):
            return [
                (row_idx, col_idx)
                for row_idx in range(len(self.board_state))
                for col_idx in range(len(self.board_state[0]))
                if self.board_state[row_idx][col_idx] == 0 or
                (abs(self.board_state[row_idx][col_idx]) /
                 self.board_state[row_idx][col_idx]) == self.player
            ]

        def generate_children(self):
            next_player = -self.player
            possible_moves = self.get_valid_moves()

            if not possible_moves or self.depth_level >= self.tree_height - 1:
                return False

            for move in possible_moves:
                row, col = move
                updated_board = copy_board(self.board_state)
                updated_board[row][col] += self.player

                overflow_queue = Queue()
                overflow(updated_board, overflow_queue)

                child_node = GameTree.Node(
                    updated_board, self.depth_level + 1, next_player, self.tree_height)
                child_node.previous_move = move
                self.child_nodes.append(child_node)

            return True

    def __init__(self, board, player, tree_height=4):
        self.player = player
        self.initial_board = copy_board(board)
        self.root_node = GameTree.Node(
            self.initial_board, 0, self.player, tree_height)
        self.minimax(self.root_node, player)

    def minimax(self, node, player):
        if node.generate_children():
            best_score = float(
                '-inf') if node.depth_level % 2 == 0 else float('inf')

            for child_node in node.child_nodes:
                child_score = self.minimax(child_node, player)

                if node.depth_level % 2 == 0:  # maximizing player
                    if child_score > best_score:
                        node.best_move = child_node.previous_move
                        best_score = child_score
                else:  # minimizing player
                    if child_score < best_score:
                        node.best_move = child_node.previous_move
                        best_score = child_score

            node.node_score = best_score
        else:
            node.node_score = evaluate_board(node.board_state, player)

        return node.node_score

    def get_move(self):
        return self.root_node.best_move

    def clear_tree(self):
        self.root_node = None
