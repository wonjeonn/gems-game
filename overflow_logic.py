from custom_data_structures import Queue


def get_overflow_list(grid):
    rows = len(grid)
    cols = len(grid[0])
    overflow_list = []
    for i in range(rows):
        for j in range(cols):
            neighbors = 0
            if i == 0 or i == rows - 1:
                if j == 0 or j == cols - 1:
                    neighbors = 2
                else:
                    neighbors = 3
            elif j == 0 or j == cols - 1:
                neighbors = 3
            else:
                neighbors = 4

            if abs(grid[i][j]) >= neighbors:
                overflow_list.append((i, j))

    return overflow_list if overflow_list else None


def check_same_sign(grid):
    value_sign = None
    for row in grid:
        for cell in row:
            if cell != 0:
                if value_sign is None:
                    value_sign = 1 if cell > 0 else -1
                elif (cell > 0 and value_sign > 0) or (cell < 0 and value_sign < 0):
                    continue
                else:
                    return False
    return True


def overflow(grid, a_queue):
    overflow_list = get_overflow_list(grid)

    if not overflow_list or check_same_sign(grid):
        return 0

    new_grid = [[cell for cell in row] for row in grid]
    for i, j in overflow_list:
        value_sign = -1 if grid[i][j] < 0 else 1
        neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        for neighbor_row, neighbor_col in neighbors:
            if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
                grid[neighbor_row][neighbor_col] = (
                    abs(grid[neighbor_row][neighbor_col]) + 1) * value_sign

    for i, j in overflow_list:
        grid[i][j] -= new_grid[i][j]

    copied_grid = [row[:] for row in grid]

    a_queue.enqueue(copied_grid)

    return 1 + overflow(grid, a_queue)
