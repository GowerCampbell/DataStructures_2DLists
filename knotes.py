# Data Structures - 2D Lists
# Written by Gower Campbell

# Fundamental data structures in Python: 2D Lists as grids or nested lists.
# Essentially, a 2D list is a list of lists, where every element of the main list is another list.

# Exploring 2D List Use
# In Python, a typical list stores multiple pieces of information in a linear order, which you can think of as a single row.
# A 2D list expands this concept to another dimension.

# Common uses for 2D lists:
# - Images: Pixels are arranged in rows and columns.
# - Board games: Spaces on a board are arranged in rows and columns.

# Each pixel can have a color value defining its shade of grey:
# - 0 represents black.
# - 255 represents white.
# - Values between 0 and 255 represent varying shades of grey.

# Example Grayscale Image:
grayscale_image = [
    [236, 189, 189, 0],
    [236, 80, 189, 189],
    [236, 0, 189, 80],
    [236, 189, 189, 80],
]

# In this 4x4 grid of pixels:
# - Each inner list represents a row.
# - Each element within these inner lists represents a column.
# This structure allows you to manipulate the pixel colors of an image easily.

# Declaring and Creating 2D Lists

# Static Declaration:
# Each element in the grid is explicitly declared.
grayscale_image = [
    [236, 189, 189, 0],
    [236, 80, 189, 189],
    [236, 0, 189, 80],
    [236, 189, 189, 80]
]

# Dynamic Declaration:
# To create an empty grid (e.g., a grid filled with None values), 
# specify the number of rows and columns.
number_of_rows = 3
number_of_columns = 2
empty_grid = [[None for _ in range(number_of_columns)] for _ in range(number_of_rows)]
print(empty_grid)  # Output: [[None, None], [None, None], [None, None]]

# Assigning Values to Elements in a 2D List
# As with a single-dimensional list, use indices to access elements.
# In a 2D list, two sets of indices are required.

# Example:
# Assign the number 4 to the element in the second row and first column of a grid named "table".
# (Remember that rows and columns are zero-indexed.)
table = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
table[1][0] = 4  # Second row, first column
print(table)

# Accessing Values:
# Example: Assign the value of the last pixel in "grayscale_image" to a variable.
last_pixel = grayscale_image[3][3]
print(last_pixel)  # Output: 80

# Looping Through Grids
# Example: Represent a school term with rows as terms and columns as test scores.
student_scores = [
    [72, 65, 78, 90, 69],
    [58, 76, 67, 67, 49],
    [97, 96, 95, 94, 93],
    [90, 93, 91, 90, 94]
]

row_index = 0
for row in student_scores:  # Outer loop for rows
    print(f"Term {row_index + 1}:")
    row_index += 1  # Increment row index
    for col in row:  # Inner loop for columns
        print(f"{col}%", end=" ")
    print()  # Newline after each term

# Handling Ragged 2D Lists
# A 2D list can have rows of varying lengths. Such lists are called "ragged lists."
ragged_list = [
    [1, 2, 3],
    [4, 5],
    [6],
    [7, 8, 9, 10]
]

# Iterating through a ragged list:
rows = len(ragged_list)
for row in range(rows):
    cols = len(ragged_list[row])  # Number of columns depends on the current row's length
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(ragged_list[row][col], end=" ")
    print()

# Trace Table Example:
matrix = [
    [1, 2, 3],  # Row 0
    [4, 5, 6],  # Row 1
    [7, 8, 9]   # Row 2
]

for i in range(3):
    for j in range(3):
        print(matrix[i][j], end=" ")
    print()

# Additional Example with Ragged List:
grid = [
    [0, 1, 2],
    [3, 4],
    [5, 6, 7, 8]
]

for row in grid:
    limit = len(row)
    for c in range(limit):
        print(row[c], end=" ")
    print()

print(grid[1])    # Output: [3, 4]
print(grid[1:])   # Output: [[3, 4], [5, 6, 7, 8]]
