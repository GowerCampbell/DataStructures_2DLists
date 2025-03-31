# Research how to populate it to create an input grid with mines on it.
# Asking how big you want the minefield you want it to be.
# Creating random mines on the grid to start with that.

import matplotlib.pyplot as plt

# Original greyscale image with some values exceeding 255
greyscale_image = [
    [235, 345, 345, 0],
    [236, 80, 125, 70],
    [256, 322, 120, 0]
]

# Display the original greyscale image
plt.imshow(greyscale_image, cmap='gray')
plt.title("Original Greyscale Image")
plt.show()

# Normalize the greyscale image to ensure values are within [0, 255]
greyscale_image = [
    [min(max(pixel, 0), 255) for pixel in row] 
    for row in greyscale_image
]

# Display the normalized greyscale image
plt.imshow(greyscale_image, cmap='gray')
plt.title("Normalized Greyscale Image")
plt.show()

# Define dimensions
number_of_rows = 3
number_of_columns = 4

# Create an empty grid
empty_grid = [[None] * number_of_columns for _ in range(number_of_rows)]

# Copy the normalized greyscale image to the empty grid
for i in range(number_of_rows):
    for j in range(number_of_columns):
        empty_grid[i][j] = greyscale_image[i][j]

# Print the normalized greyscale image
print("Normalized Greyscale Image:")
for row in greyscale_image:
    print(row)

# Print the empty grid (after copying)
print("\nEmpty Grid (after copying):")
for row in empty_grid:
    print(row)

# Create a binary image using a threshold of 128
threshold = 128
binary_image = [
    [1 if pixel > threshold else 0 for pixel in row] 
    for row in greyscale_image
]

# Display the binary image
plt.imshow(binary_image, cmap='gray')
plt.title("Binary Image (Threshold = 128)")
plt.show()

# Print the binary image
print("\nBinary Image:")
for row in binary_image:
    print(row)
import copy

# A deep copy creates a completely independent copy of a data structure, including 
# all nested objects. This means changes to the original structure do not affect the copy.

# In contrast:

# A shallow copy only copies references to nested objects, meaning changes 
# to the nested objects in one structure affect the other.


def process_grid(grid):
    # Create a new result grid
    result_grid = [[0, 2, 0],
                   [0, 0, 0],
                   [0, 0, 0]]

    # Use deep copy to ensure changes to 'end_grid' do not affect 'grid'
    end_grid = copy.deepcopy(grid)
    
    # Example: Modifying a value
    end_grid[2][2] = 1

    return end_grid

print("Start Grid:", start_grid)  # Unchanged
print("New Grid:", new_grid)      # Modified


def count_surrounding_non_zero(grid, row=1, col=1):
    
    
    directions = [(-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
                  (0, -1),         (0, 1),     # Left, Right
                  (1, -1), (1, 0), (1, 1)]    # Bottom-left, Bottom, Bottom-right
    count = 0

for direcy_row, direct_column in directions:
    new_row = row + direct_row
    new_col = col + direct_column

    if 0 <= new_row <3 and 0 <= new_col < 3:
        if grid[new_row][new_col] != 0:
            count 


surrounding_count = 0  # Initialize the count of non-zero neighbors
row_num = len(grid)    # Get the number of rows in the grid
col_num = len(grid[0]) # Get the number of columns in the grid


# Example usage
def create_grid(grid):
    # Step 1: Initialize a start grid
    result_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # A static grid with zeros

    # Step 2: Process the grid (calling process_grid)
    new_grid = process_grid(start_grid)  
    # This will call another function process_grid and pass the start_grid

    # Step 3: Determine grid dimensions (rows and columns)
    row_num = len(grid)  # Get the number of rows in the input grid
    col_num = len(grid[0])  # Get the number of columns in the first row

    # Step 4: Iterate through each element in the grid
    for row in range(row_num):  # Loop through each row
        for col in range(col_num):  # Loop through each column in the row

            # Step 5: If the current grid element is zero, we process its neighbors
            if grid[row][row] == 0:  # This seems to be a mistake (should likely be grid[row][col])
                surrounding_count = count_surronding_non_zero(grid, row, col_num)  
                # Counting non-zero neighbors
                
                # Step 6: Update result_grid with surrounding counts
                result_grid[row][col] = surrounding_count
            else:
                result_grid[row][col] = surrounding_count 
                 # Update with last count of surrounding non-zero (mistake)
  
        return result_grid




