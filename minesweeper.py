
# Learning Objectives:
# - Work with 2D Lists and learn how to access and modify key elements.

# - Learn how create nested loops to iterate over rows and columns.

# - Introduce randomness to place mines and control their probability.

# - Implement boundary checks to avoid errors when accessing rows and columns.


# - Break the problem into reusable functions (e.g. count_adjacent_mines, 
#   create_random_grid))

# Written by Gower Campbell.

import random

def create_random_grid(rows, cols, mine_probability=0.2):
    """
    Creates a random Minesweeper grid with mines and mine-free spots.

    Parameters:
    - rows (int): The number of rows in the grid.
    - cols (int): The number of columns in the grid.
    - mine_probability (float): The probability of a cell being a mine 
                               (default is 0.2).

    Returns:
    - list of list of str: A 2D list representing the Minesweeper grid.
    """
    grid = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            # Randomly decides if the cell is a mine based on set probability
            if random.random() < mine_probability:
                row.append("#")  # Mine
            else:
                row.append("-")  # Mine-free spot
        grid.append(row)
    return grid

def count_adjacent_mines(grid, row, col):
    """
    Counts the number of mines to a specific cell in the grid.

    Parameters:
    - grid ( a list of a list set to str): Representing the Minesweeper grid.
    - row (int): The row index of the cell to check.
    - col (int): The column index of the cell to check.

    Returns:
    - int: The number of mines adjacent to the cell at (row, col).
    """
    # Directions for checking adjacent cells 
    # (8 directions: NW, N, NE, W, E, SW, S, SE)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # NW, N, NE
        (0, -1),          (0, 1),    # W,     E
        (1, -1), (1, 0), (1, 1)      # SW, S, SE
    ]
    count = 0  # Initialize's the count of mines

    # Loops through all directions to check the cells
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc  # Calculate's a new position

        # Checks if the new position is within the bounds of the grid.
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            # If the adjacent cell contains a mine ("#"), increments the count
            if grid[new_row][new_col] == "#":
                count += 1

    return count

def reveal_cell(grid, visible_grid, row, col):
    """
    Reveals a cell in the grid and updates the visible grid.

    Parameters:
    - grid (list of list set of str): The grid with mines and counts.
    - visible_grid (list of list set of str): The grid visible to the player.
    - row (int): The row index of the cell to reveal.
    - col (int): The column index of the cell to reveal.

    Returns:
    - bool: True if the revealed cell is a mine, False otherwise.
    """
    if grid[row][col] == "#":
        visible_grid[row][col] = "#"  # Reveal the mine
        return True  # Player hit a mine
    else:
        # Update the visible grid with the mine count
        visible_grid[row][col] = str(count_adjacent_mines(grid, row, col))
        return False

def print_grid(grid):
    """
    Prints the grid in a readable format with row and column numbers.

    Parameters:
    - grid (list of list of str/int): The 2D list representing the grid.
    """
    # Print column numbers (right-aligned)
    print("    " + "  ".join(f"{i:>2}" for i in range(len(grid[0]))))

    # Print each row with its row number
    for row_idx, row in enumerate(grid):
        # Format each cell to take up 2 spaces and right-align
        formatted_row = "  ".join(f"{cell:>2}" for cell in row)
        print(f"{row_idx:>2}  {formatted_row}")

def mark_mines(grid, visible_grid):
    """
    Marks the locations of mines on the visible grid.

    Parameters:
    - grid (list of list of str): The original grid with mines.
    - visible_grid (list of list of str): The grid visible to the player.
    """
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                visible_grid[row][col] = "#"  # Mark the mine

def play_minesweeper(rows, cols, mine_probability=0.2):
    """
    Playable Minesweeper game.

    Parameters:
    - rows (int): The number of rows in the grid.
    - cols (int): The number of columns in the grid.
    - mine_probability (float): The probability of a cell being a mine.
    """
    # Creates the original grid with mines
    grid = create_random_grid(rows, cols, mine_probability)

    # Creates a grid for the player (all cells hidden, represented by "-")
    visible_grid = [["-" for _ in range(cols)] for _ in range(rows)]

    # Introduces lives: Player starts with 3 lives
    lives = 3

    # Flag to control the game loop
    game_over = False

    # Game loop
    while not game_over:
        print("\nMinesweeper:")
        print("Will you survive?")
        print(f"\nLives remaining: {lives}")
        print("------------------>")
        print_grid(visible_grid)

        # Get player input
        try:
            row = int(input("\nEnter row number: "))
            col = int(input("Enter column number: "))
        except ValueError:
            print("\nInvalid input! Please enter numbers.")
            continue

        # Check if the input is within bounds
        if row < 0 or row >= rows or col < 0 or col >= cols:
            print("\nInvalid row or column! Try again.")
            continue

        # Reveal the cell
        if reveal_cell(grid, visible_grid, row, col):
            lives -= 1  # Decrease lives when the player hits a mine
            print("\nYou hit a mine!")
            if lives == 0:  # Check if the player has run out of lives
                print("\nGame Over! You've run out of lives.")
                mark_mines(grid, visible_grid)  # Mark all mines
                print("\nFinal Grid:")
                print_grid(visible_grid)
                game_over = True
            else:
                print(f"Lives remaining: {lives}")
        else:
            # Check if the player has won
            if all(cell != "-" for row in visible_grid for cell in row):
                print("\nCongratulations! You've cleared the grid.")
                mark_mines(grid, visible_grid)  # Mark all mines
                print("Final Grid:")
                print_grid(visible_grid)
                game_over = True

# Start the game
rows = 5
cols = 5
mine_probability = 0.2  # 20% chance of a cell being a mine
play_minesweeper(rows, cols, mine_probability)

#<----- Reflections -------->

# Applying towards my programming skills, particularly in working with 
# 2D lists and nested loops to manage grids. I gained alot from using the 
# random module to introduce unpredictability into my code and learned the 
# importance of boundary checks to handle edge cases to prevent index errors.

# Finding and maintaining my program, while testing and debugging helped me 
# better visualise data through printed grids and refining my approach by 
# breaking the task down into manageable steps.

"""
<----Biblography --->
- Python: Syntax and Structures:
https://docs.python.org/3/library/
- Python: Generating pseudo-random numbers.
https://docs.python.org/3/library/random.html
- W3schools Python 2D lists and grids 
https://www.w3schools.com/python/python_lists.asp
-GeeksforGeeks: Handling IndexError
https://www.geeksforgeeks.org/python-handling-indexerror/
- StackOverflow: Minesweeper Challenge
https://stackoverflow.com/questions/70283421/minesweeper-python-coding-challenge
"""







