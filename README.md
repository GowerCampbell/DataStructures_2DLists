# **Mastering 2D Lists in Python: A Learning Module**

## **📌 Introduction**  
Welcome to this in-depth learning module on **2D Lists**—a key data structure in Python, also known as grids or nested lists. This guide takes you through everything I’ve learned about 2D lists, from their basics to their application in HyperionDev’s **Minesweeper task**. Using my own notes and examples, I’ll show you how to create, manipulate, and traverse 2D lists, culminating in a fully functional Minesweeper game. Whether you’re a beginner or refining your skills, this module will equip you with a solid understanding of 2D lists.

🔗 **[View Full Code](https://github.com/GowerCampbell/minesweeper.git)**  
🔗 **[Minesweeper Game](https://github.com/GowerCampbell/minesweeper/blob/main/main.py)**  

---

## **🎯 What You’ll Learn**  
This module is based on my journey with HyperionDev’s curriculum and my own explorations. Here’s what I aimed to master:  
- **Understanding 2D Lists**: How they’re structured as lists of lists.  
- **Creating Grids**: Static and dynamic methods with examples like grayscale images.  
- **Accessing & Modifying**: Using indices to work with rows and columns.  
- **Nested Loops**: Iterating over grids, including ragged ones.  
- **Boundary Checks**: Preventing errors when accessing adjacent cells.  
- **Randomization**: Adding unpredictability with Python’s `random` module.  
- **Application**: Building a Minesweeper game from HyperionDev’s task.  

---

## **📚 Understanding 2D Lists**  
A 2D list is a list where each element is another list—essentially a grid with rows and columns. My notes describe it as “a list of lists, where every element of the main list is another list.” This structure is perfect for representing structured data like images or game boards.

### **Basic Example**  
```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(grid[1][0])  # Output: 4 (second row, first column)
```
- **Rows**: 3 (each inner list).  
- **Columns**: 3 (elements per row).  
- **Structure**: `grid[row][column]` accesses specific elements.  

### **Why 2D Lists Matter**  
My notes highlight common uses:  
- **Images**: “Pixels are arranged in rows and columns.” For example, a grayscale image uses numbers (0 = black, 255 = white) to represent shades.  
- **Board Games**: “Spaces on a board are arranged in rows and columns,” like Minesweeper.  

---

## **🔧 Creating 2D Lists: Static and Dynamic Approaches**  

### **Static Declaration**  
When you know the values upfront, you can hardcode them. My notes include this grayscale image example:  
```python
grayscale_image = [
    [236, 189, 189, 0],
    [236, 80, 189, 189],
    [236, 0, 189, 80],
    [236, 189, 189, 80]
]
print(grayscale_image[0])  # Output: [236, 189, 189, 0]
```
- **Details**: Each inner list is a row, each number a column (pixel).  
- **Reflection**: “This structure allows you to manipulate the pixel colors of an image easily.”  

### **Dynamic Declaration**  
For flexibility, I learned to create grids programmatically. Here’s an example from my notes:  
```python
number_of_rows = 3
number_of_columns = 2
empty_grid = [[None for _ in range(number_of_columns)] for _ in range(number_of_rows)]
print(empty_grid)  # Output: [[None, None], [None, None], [None, None]]
```
- **How It Works**: The inner comprehension creates columns, the outer one repeats it for rows.  
- **Note**: You can replace `None` with any value (e.g., `0`, `" "`).  
- **Reflection**: “I gained a lot from breaking the task down into manageable steps,” like this grid setup.  

See this in action in **[grid_utils.py](https://github.com/GowerCampbell/minesweeper/blob/main/grid_utils.py)** with `create_random_grid()`.  

---

## **🔧 Working with Elements: Accessing and Modifying**  

### **Accessing Values**  
My notes explain: “As with a single-dimensional list, use indices to access elements, but in a 2D list, two sets of indices are required.”  
```python
last_pixel = grayscale_image[3][3]
print(last_pixel)  # Output: 80
```
- **Details**: `[3][3]` targets the fourth row, fourth column (zero-indexed).  

### **Modifying Values**  
Assigning new values is straightforward:  
```python
table = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
table[1][0] = 4  # Second row, first column
print(table)  # Output: [[0, 0, 0], [4, 0, 0], [0, 0, 0]]
```
- **Reflection**: “This taught me how to access and modify key elements,” a skill I used in Minesweeper.  

---

## **🔧 Traversing Grids with Nested Loops**  

### **Standard Grids**  
My notes use a student scores example to show nested loops:  
```python
student_scores = [
    [72, 65, 78, 90, 69],
    [58, 76, 67, 67, 49],
    [97, 96, 95, 94, 93],
    [90, 93, 91, 90, 94]
]
row_index = 0
for row in student_scores:
    print(f"Term {row_index + 1}:")
    row_index += 1
    for col in row:
        print(f"{col}%", end=" ")
    print()
```
- **Output**:  
  ```
  Term 1: 72% 65% 78% 90% 69% 
  Term 2: 58% 76% 67% 67% 49% 
  Term 3: 97% 96% 95% 94% 93% 
  Term 4: 90% 93% 91% 90% 94% 
  ```
- **Details**: Outer loop handles rows (terms), inner loop handles columns (scores).  
- **Reflection**: “I learned how to create nested loops to iterate over rows and columns.”  

### **Ragged Lists**  
My notes also cover uneven grids:  
```python
ragged_list = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]
rows = len(ragged_list)
for row in range(rows):
    cols = len(ragged_list[row])
    print(f"Row {row} has {cols} columns: ", end="")
    for col in range(cols):
        print(ragged_list[row][col], end=" ")
    print()
```
- **Output**:  
  ```
  Row 0 has 3 columns: 1 2 3 
  Row 1 has 2 columns: 4 5 
  Row 2 has 1 columns: 6 
  Row 3 has 4 columns: 7 8 9 10 
  ```
- **Details**: Each row’s length is checked to avoid errors.  
- **Reflection**: “Iterating through a ragged list is trickier,” but it taught me adaptability.  

Check this technique in **[display.py](https://github.com/GowerCampbell/minesweeper/blob/main/display.py)** with `print_grid()`.  

---

## **🔧 Handling Boundaries**  
When checking adjacent cells, boundary validation is crucial. My notes emphasize: “I learned the importance of boundary checks to handle edge cases to prevent index errors.”  
```python
grid = [[1, 2, 3], [4, 5, 6]]
row, col = 0, 1
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
for dr, dc in directions:
    r, c = row + dr, col + dc
    if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
        print(f"Adjacent at ({r}, {c}): {grid[r][c]}")
```
- **Output**:  
  ```
  Adjacent at (0, 0): 1
  Adjacent at (0, 2): 3
  Adjacent at (1, 0): 4
  Adjacent at (1, 1): 5
  Adjacent at (1, 2): 6
  ```
- **Details**: Only valid indices are accessed, skipping out-of-bounds positions.  

See this in **[grid_utils.py](https://github.com/GowerCampbell/minesweeper/blob/main/grid_utils.py)** with `count_adjacent_mines()`.  

---

## **🔧 Randomization with 2D Lists**  
My notes mention: “I gained a lot from using the random module to introduce unpredictability into my code.” Here’s how I applied it:  
```python
import random
rows, cols = 3, 3
grid = [["#" if random.random() < 0.3 else "-" for _ in range(cols)] for _ in range(rows)]
for row in grid: print(row)
```
- **Sample Output**:  
  ```
  ['-', '#', '-']
  ['#', '-', '-']
  ['-', '-', '#']
  ```
- **Details**: Each cell has a 30% chance of being a mine (`#`).  
- **Reflection**: “This was key for Minesweeper’s random mine placement.”  

---

## **🏆 Applying It All: HyperionDev’s Minesweeper Task**  
HyperionDev tasked me with processing a grid of `#` (mines) and `-` (safe spots), replacing each `-` with the count of adjacent mines.

### **Task Example**  
**Input**:  
```python
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"]
]
```
**Expected Output**:  
```python
[
    [1, 1, 2, "#", "#"],
    [1, "#", 3, 2, 1],
    [1, 2, "#", 1, 0]
]
```

### **My Solution**  
```python
def process_minesweeper(grid):
    rows, cols = len(grid), len(grid[0])
    result = [row[:] for row in grid]
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "-":
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "#":
                        count += 1
                result[r][c] = count
    return result

grid = [["-", "-", "-", "#", "#"], ["-", "#", "-", "-", "-"], ["-", "-", "#", "-", "-"]]
result = process_minesweeper(grid)
for row in result: print(row)
```
- **How It Works**:  
  - Copies the grid to preserve the original.  
  - Uses nested loops to check each cell.  
  - Counts mines in 8 directions with boundary checks.  
- **Reflection**: “Breaking the problem into reusable functions like this made it manageable.”  

---

## **🎮 Building Minesweeper: Putting It Together**  
Using these skills, I built a playable Minesweeper game.

### **Project Structure**  
```
minesweeper/
├── main.py          # Game loop and logic -> [View](https://github.com/GowerCampbell/minesweeper/blob/main/main.py)
├── grid_utils.py    # Grid creation and helpers -> [View](https://github.com/GowerCampbell/minesweeper/blob/main/grid_utils.py)
├── display.py       # Grid printing -> [View](https://github.com/GowerCampbell/minesweeper/blob/main/display.py)
├── tests/           # Unit tests
│   └── test_grid.py # Tests -> [View](https://github.com/GowerCampbell/minesweeper/blob/main/tests/test_grid.py)
└── README.md        # This module
```

### **Key Implementations**  
#### **Grid Creation**  
```python
# grid_utils.py
import random

def create_random_grid(rows, cols, mine_probability=0.2):
    grid = []
    for _ in range(rows):
        row = ["#" if random.random() < mine_probability else "-" for _ in range(cols)]
        grid.append(row)
    return grid
```
- **Details**: “Randomly decides if the cell is a mine based on set probability.”  

#### **Counting Mines**  
```python
# grid_utils.py
def count_adjacent_mines(grid, row, col):
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    count = 0
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            if grid[new_row][new_col] == "#":
                count += 1
    return count
```
- **Details**: “Counts the number of mines adjacent to a specific cell in the grid.”  

#### **Game Loop**  
```python
# main.py
from grid_utils import create_random_grid, count_adjacent_mines
from display import print_grid

def play_minesweeper(rows, cols, mine_probability=0.2):
    grid = create_random_grid(rows, cols, mine_probability)
    visible_grid = [["-" for _ in range(cols)] for _ in range(rows)]
    lives = 3
    game_over = False
    while not game_over:
        print_grid(visible_grid)
        try:
            row, col = map(int, input("\nEnter row, col: ").split())
            if row < 0 or row >= rows or col < 0 or col >= cols:
                print("Invalid input!")
                continue
            if grid[row][col] == "#":
                visible_grid[row][col] = "#"
                lives -= 1
                if lives == 0:
                    print("Game Over!")
                    game_over = True
            else:
                visible_grid[row][col] = str(count_adjacent_mines(grid, row, col))
        except ValueError:
            print("Enter numbers!")
    for row in visible_grid: print(row)

play_minesweeper(5, 5)
```
- **Details**: Includes a lives system (my addition) and basic interactivity.  

---

## **📊 Reflections**  
From my notes:  
- “Applying towards my programming skills, particularly in working with 2D lists and nested loops to manage grids.”  
- “Finding and maintaining my program, while testing and debugging, helped me better visualize data through printed grids.”  
- “I gained a lot from using the random module to introduce unpredictability into my code and learned the importance of boundary checks.”  

---

## **🚀 Next Steps**  
- **Enhance Minesweeper**: Add recursion for flood-fill revealing (see my earlier attempts).  
- **Image Processing**: Use 2D lists with `matplotlib` for grayscale images (from my notes).  
- **Dynamic Sizing**: Ask users for grid dimensions, as I researched.  

---

## **📚 Resources**  
- **[Python Docs – Lists](https://docs.python.org/3/tutorial/datastructures.html)**  
- **[Python – Random](https://docs.python.org/3/library/random.html)**  
- **[W3Schools – Lists](https://www.w3schools.com/python/python_lists.asp)**  
- **[GeeksforGeeks – IndexError](https://www.geeksforgeeks.org/python-handling-indexerror/)**  
- **[Stack Overflow – Minesweeper](https://stackoverflow.com/questions/70283421/minesweeper-python-coding-challenge)**  


