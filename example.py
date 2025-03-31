# Find each zero position
# Go through each adjacent position.
# Looking at how many non-zeros exist.

def process_grid(grid):
    result_grid = [row[:] for row in grid]  # Make a deep copy of the grid
    # Step 1: navigating the grid
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 0:
                # Step 2: Find adjacent positions.
                count = count_adjacent(grid, row, col)
                result_grid[row][col] = count
            else:
                result_grid[row][col] = grid[row][col]
    return result_grid

def count_adjacent(grid, row, col):
    coordinates = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for coor_row, coor_col in coordinates:
        new_row = row + coor_row
        new_col = col + coor_col

        # Step 3: validating index boundaries.
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            if grid[new_row][new_col] != 0:
                count += 1
    return count

def main():
    grid = [
        [0, 2, 0],
        [3, 0, 1],
        [0, 5, 6]
    ]

    result_grid = process_grid(grid)
    print("Processed Grid:")
    for row in result_grid:
        print(row)

if __name__ == "__main__":
    main()


# # 1. Goal of the Code
# We want to process a 3x3 grid.
# For every 0 in the grid:
# Count the number of non-zero neighbors in the adjacent cells (diagonally, horizontally, and vertically).
# Replace the 0 in the grid with that count.

# 2. Functions in the Code
# A. process_grid(grid)
# This function:

# Takes a 3x3 grid as input.
# Loops through every cell in the grid using two for loops:
# row for rows (0 to 2).
# col for columns (0 to 2).
# If a cell contains 0:
# Calls the count_adjacent function to count its non-zero neighbors.
# Updates the value of the cell in a copy of the grid (result_grid) with the count.
# If the cell isn’t 0, it keeps the original value.
# Returns the updated grid.

# B. count_adjacent(grid, row, col)
# This function:

# Checks all adjacent positions (diagonal, horizontal, and vertical 
# neighbors) of a cell at position (row, col).
# It uses a list of relative coordinates to find the neighbors:
# python

# Each tuple represents the relative position of a neighbor. 
# For example, (-1, 0) means "one row above, same column."
# For each coordinate:
# It calculates the actual position of the neighbor: (new_row, new_col).
# It ensures the neighbor is within the grid's boundaries (0 to 2 for both rows and columns).
# If the neighbor isn’t 0, it increases the count.
# Returns the total count of non-zero neighbors.


# Certainly! Let’s continue the breakdown:

# 3. Step-by-Step Example (Continued)
# Input Grid
# python
# Copy code
# [
#     [0, 2, 0],
#     [3, 0, 1],
#     [0, 5, 6]
# ]
# Step 1: Processing the Grid
# Outer Loop
# The process_grid() function loops over each cell in the grid using row and col.
# For each cell:

# Cell (0, 0):
# Value is 0.
# Call count_adjacent() to count non-zero neighbors:
# Neighbors: (0, 1) (value 2), (1, 0) (value 3), (1, 1) (value 0).
# Non-zero neighbors: 2 (values 2 and 3).
# Update the value of (0, 0) in result_grid to 2.

# Cell (0, 1):
# Value is 2 (non-zero).
# Keep the original value.
# result_grid[0][1] = 2.
# Cell (0, 2):

# Value is 0.
# Call count_adjacent() to count non-zero neighbors:
# Neighbors: (0, 1) (value 2), (1, 1) (value 0), (1, 2) (value 1).
# Non-zero neighbors: 2 (values 2 and 1).
# Update the value of (0, 2) in result_grid to 2.

# Cell (1, 0):
# Value is 3 (non-zero).
# Keep the original value.
# result_grid[1][0] = 3.

# Cell (1, 1):
# Value is 0.

# Call count_adjacent() to count non-zero neighbors:
# Neighbors: (0, 0) (value 2), (0, 1) (value 2), (0, 2) 
# (value 2), (1, 0) (value 3), (1, 2) (value 1), (2, 0) 
# (value 0), (2, 1) (value 5), (2, 2) (value 6).
# Non-zero neighbors: 6 (values 2, 2, 2, 3, 1, 5, 6).
# Update the value of (1, 1) in result_grid to 6.

# Cell (1, 2):
# Value is 1 (non-zero).
# Keep the original value.
# result_grid[1][2] = 1.

# Cell (2, 0):
# Value is 0.
# Call count_adjacent() to count non-zero neighbors:
# Neighbors: (1, 0) (value 3), (1, 1) (value 6), (2, 1) (value 5).
# Non-zero neighbors: 3 (values 3, 6, 5).
# Update the value of (2, 0) in result_grid to 3.

# Cell (2, 1):
# Value is 5 (non-zero).
# Keep the original value.
# result_grid[2][1] = 5.

# Cell (2, 2):
# Value is 6 (non-zero).
# Keep the original value.
# result_grid[2][2] = 6.

# Step 2: Final Processed Grid
# After all the cells are processed, the final result_grid becomes:

# python
# Copy code
# [
#     [2, 2, 2],
#     [3, 6, 1],
#     [3, 5, 6]
# ]
# Step 3: Output
# The main() function prints the grid row by row:


# Output
# Processed Grid:
# [2, 2, 2]
# [3, 6, 1]
# [3, 5, 6]

# Key Concepts in the Code
# Grid Navigation:

# Use nested loops (row and col) to traverse a 2D grid.
# Neighbor Calculation:

# Use relative coordinates to find adjacent cells.
# Boundary Validation:

# Ensure neighbors are within valid grid limits.
# Deep Copy:

# Copy the grid properly to avoid modifying the original during processing.
# By breaking down the logic and the grid updates 
# step-by-step, we ensure the program behaves as intended! 😊






