# Data Structures & 2D Lists (Minesweeper Project)

## **📌 Overview**  
Welcome to my learning journey into **Data Structures**, where I dive deep into **2D Lists (Grids/Nested Lists)** by creating a fully functional **Minesweeper Game** in Python. This project serves as both a practical application and a personal exploration of how 2D lists can model real-world problems like game boards and image grids. Through this process, I’ve tackled nested loops, recursion, randomization, and game logic—building a solid foundation in Python’s data manipulation capabilities.

🔗 **[View Full Code](https://github.com/GowerCampbell/minesweeper.git)** | 🔗 **[Live Demo](#)** *(Coming soon with GUI integration!)*  

---

## **🎯 Learning Objectives**  
This project was designed to solidify my understanding of key programming concepts while pushing me to apply them creatively. Here’s what I aimed to achieve:  
✔ **Master 2D Lists** – Grasp how grids are structured in Python, including rows, columns, and indexing techniques.  
✔ **Nested Loops** – Gain fluency in iterating over 2D structures for traversal and manipulation.  
✔ **Boundary Checks** – Learn to handle edge cases and prevent index errors with robust validation.  
✔ **Randomization** – Leverage Python’s `random` module to dynamically place mines, introducing unpredictability.  
✔ **Recursive Algorithms** – Implement flood-fill recursion to reveal empty cells efficiently.  
✔ **Game Logic** – Build a playable game with mine tracking, flagging, and win/loss conditions.  

Each objective was a stepping stone toward creating a functional Minesweeper game while deepening my programming skills.

---

## **📂 Project Structure**  
The repository is organized for clarity and modularity, making it easy to navigate and extend:  
```
minesweeper/
├── main.py                # Core game logic and entry point
├── utils.py               # Helper functions (e.g., grid creation, printing)
├── tests/                 # Unit tests for key functions
│   └── test_minesweeper.py
└── README.md              # Detailed project documentation
```

- **`main.py`**: Houses the game loop, user interaction, and primary logic.  
- **`utils.py`**: Contains reusable functions like `create_grid()` and `print_grid()`.  
- **`tests/`**: Includes basic unit tests to ensure functionality (e.g., mine counting, boundary checks).  

---

## **🔧 Key Implementations**  

### **1️⃣ Creating the Minefield**  
The foundation of Minesweeper is a 2D grid with randomly placed mines. I used a list comprehension for efficiency:  
```python
import random

def create_grid(rows, cols, mine_prob=0.2):
    """Generates a minesweeper grid with random mines ('#') and safe spots ('-')."""
    return [
        ["#" if random.random() < mine_prob else "-" 
         for _ in range(cols)] 
        for _ in range(rows)
    ]
```
- **How it Works**: Each cell has a `mine_prob` chance (default 20%) of being a mine (`#`). Otherwise, it’s safe (`-`).  
- **Learning Takeaway**: List comprehensions simplified grid creation, reducing code verbosity.

### **2️⃣ Counting Adjacent Mines**  
To display numbers indicating nearby mines, I checked all eight adjacent cells:  
```python
def count_adjacent_mines(grid, row, col):
    """Counts mines in all 8 directions around a cell."""
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "#":
            count += 1
    return count
```
- **How it Works**: Iterates through a list of direction tuples, checks bounds, and counts mines.  
- **Learning Takeaway**: Boundary checking was critical to avoid `IndexError`s, reinforcing the importance of validation.

### **3️⃣ Revealing Cells (Recursive Flood Fill)**  
When a player reveals an empty cell, adjacent safe cells should cascade open:  
```python
def reveal_cell(grid, visible, row, col):
    """Reveals a cell and recursively uncovers adjacent safe cells."""
    if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or (row, col) in visible:
        return
    visible.add((row, col))
    if count_adjacent_mines(grid, row, col) == 0:
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:  # 4-directional flood fill
            reveal_cell(grid, visible, row + dr, col + dc)
```
- **How it Works**: Uses recursion to reveal neighboring cells if the current cell has no adjacent mines.  
- **Learning Takeaway**: Recursion was a game-changer—elegant yet tricky to debug without proper base cases.

### **4️⃣ Game Loop & Win Condition**  
The game loop ties everything together, handling user input and determining outcomes:  
```python
def play_game(rows=5, cols=5, mines=5):
    grid = create_grid(rows, cols)
    visible = set()
    flags = set()
    while True:
        print_grid(grid, visible, flags)
        action = input("Reveal (r) or Flag (f)? ").lower()
        row, col = map(int, input("Enter row, col: ").split())
        if action == "r":
            if grid[row][col] == "#":
                print("💥 Game Over!")
                break
            reveal_cell(grid, visible, row, col)
        elif action == "f":
            flags.add((row, col))
        if len(visible) == (rows * cols) - mines:
            print("🎉 You Win!")
            break
```
- **How it Works**: Players choose to reveal or flag cells; the game ends on a mine hit or when all safe cells are revealed.  
- **Learning Takeaway**: Managing state (revealed cells, flags) with sets was efficient and intuitive.

---

## **📊 Lessons Learned**  
This project was a goldmine of insights:  
✅ **2D List Manipulation** – I became comfortable traversing and modifying grids, a skill applicable beyond games (e.g., image processing).  
✅ **Edge Case Handling** – Boundary checks taught me to anticipate and prevent errors proactively.  
✅ **Recursive Algorithms** – Flood fill demystified recursion, showing its power and pitfalls (e.g., stack overflow risks).  
✅ **User Interaction** – Building a CLI game honed my skills in input validation and user feedback loops.  
✅ **Debugging** – Printing grids during development helped visualize data flow, making bugs easier to spot.  

One "aha!" moment was realizing how breaking the problem into smaller functions (e.g., `count_adjacent_mines`) improved readability and reusability.

---

## **🚀 Future Improvements**  
The journey doesn’t end here! I’ve got big plans to level up this project:  
🔹 **GUI Version** – Transition to a graphical interface using `pygame` or `tkinter` for a more immersive experience.  
🔹 **Difficulty Levels** – Add adjustable grid sizes and mine counts to challenge players.  
🔹 **Score Tracking** – Implement file I/O to save high scores and track progress over time.  
🔹 **Lives System** – Introduce a lives mechanic (e.g., 3 lives before game over) for added strategy.  
🔹 **Sound Effects** – Integrate audio cues (e.g., explosions) to enhance engagement.  

These enhancements will push me to explore new libraries and concepts, keeping the learning momentum going.

---

## **📚 Resources**  
I leaned on these fantastic resources to guide my journey:  
- **[Python Official Docs – Lists](https://docs.python.org/3/tutorial/datastructures.html)** – The go-to for understanding list mechanics.  
- **[Real Python – Minesweeper Tutorial](https://realpython.com/python-minesweeper/)** – Inspired my approach to game logic and recursion.  
- **[GeeksforGeeks – 2D Arrays](https://www.geeksforgeeks.org/python-using-2d-arrays-lists-the-right-way/)** – Clarified nested list syntax and pitfalls.  
- **[W3Schools – Python Lists](https://www.w3schools.com/python/python_lists.asp)** – Quick reference for list operations.  
- **[Stack Overflow – Minesweeper Challenge](https://stackoverflow.com/questions/70283421/minesweeper-python-coding-challenge)** – Community insights for troubleshooting.  

---

## **🤝 Contributing**  
I’d love for this project to grow with input from others! Here’s how you can get involved:  
1. **Fork** the repo and experiment with your own features.  
2. **Submit Pull Requests** with improvements or bug fixes.  
3. **Open Issues** for bugs or enhancement ideas.  

📧 **Contact**: [your.email@example.com]  
🔗 **LinkedIn**: [Your Profile](https://linkedin.com/in/yourprofile)  

---

## **🌟 Final Thoughts**  
Building Minesweeper was more than just a coding exercise—it was a journey of discovery. From wrestling with recursion to celebrating a working flood-fill, every step taught me something new about Python and problem-solving. If this repo helps even one person understand 2D lists better, I’ll consider it a win!

