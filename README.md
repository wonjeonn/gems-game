# **Overflow Gems Game**

**Overflow Gems Game** is a strategic board game in which players compete to dominate the board by strategically placing and overflowing gems. The game supports human and bot-controlled gameplay, combining human strategy with intelligent decision-making.

## **Features**

- **Bot Player (Player Two)**: Uses a GameTree and the minimax algorithm to make intelligent moves.
- **Game Mechanics**: Simulates gem overflow and chain reactions across a 5x6 grid.
- **Custom Data Structures**: Optimizes game logic using a HashTable, Stack, Queue, and Deque.
- **Flexible Gameplay**: Supports human vs. human, human vs. bot, and bot vs. bot modes.

## **Installation**

1. Ensure Python 3.10 or later is installed.
2. Install the required dependency:
   ```bash
   pip install pygame
   ```
3. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
4. Navigate to the project directory:

   ```bash
   cd /path/to/project
   ```

5. Launch the game:
   ```bash
   python3 game.py
   ```

## **Game Rules**

1. Players take turns placing gems on a 5x6 board.
2. A cell "overflows" when the number of gems exceeds its threshold, based on the number of adjacent cells:
   - Corners: Overflow at 2 gems.
   - Edges: Overflow at 3 gems.
   - Middle cells: Overflow at 4 gems.
3. Overflow mechanics:
   - Gems are distributed to neighbouring cells.
   - Chain reactions occur if neighbouring cells also overflow.
4. The objective is to dominate the board by owning the majority of gems in your colour.

## **Game Logic**

### **1. Bot Player Strategy**

- **Minimax Algorithm**:
  - Simulates potential board states to a specified depth.
  - Evaluates board states using a heuristic function.
  - Select moves that maximize the bot's advantage.
- **Heuristic Scoring**:
  - Considers gem counts, positional advantages, and board control.

### **2. Overflow Mechanics**

- Gems placed in a cell propagate to neighbouring cells upon overflow.
- Chain reactions occur recursively until no cell overflows.

### **3. Custom Data Structures**

- **Queue** and **Deque**: Efficiently handle overflow propagation.
- **HashTable**: Optimizes board state evaluations for better performance.
- **Stack**: Used for auxiliary calculations.

## **File Structure**

```
.
├── player_one_bot.py          # Optional bot logic for Player One
├── player_two_bot.py          # Bot logic for Player Two
├── assets/                    # Game assets (images)
├── tests/                     # Unit tests for game functionality
│   ├── hash_table_test.py     # Unit tests for HashTable implementation
│   ├── test_game_helpers.py   # Unit tests for game helpers and logic
├── custom_data_structures.py  # Custom data structures (HashTable, Stack, etc.)
├── overflow_logic.py          # Implements overflow mechanics
├── game_tree.py               # GameTree logic for bot decision-making (Minimax)
├── game.py                    # Main game logic
├── hash_table.py              # HashTable implementation
└── README.md                  # Project documentation
```

## **Acknowledgments**

- Gem images are sourced from [opengameart.org](https://opengameart.org) by **qubodup**:
  - [Rotating Crystal Animation](https://opengameart.org/content/rotating-crystal-animation-8-step)
  - Licensed under [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).
