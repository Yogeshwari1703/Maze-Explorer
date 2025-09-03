
````markdown
# 🧩 Maze Explorer: DFS vs BFS

This project is a **game-like simulation** of two classic graph traversal algorithms:  
- **Depth First Search (DFS)**  
- **Breadth First Search (BFS)**  

It allows you to visually compare how DFS and BFS explore a maze to find a path from a start node to a goal node.

---

## 🎮 How to Play
1. Run the Python script in **VS Code** (or any terminal).  
   ```bash
   python maze_explorer.py


2. A grid (maze) will appear.
3. Use **mouse clicks**:

   * **Left-click**:

     * First click = Start (Green)
     * Second click = End (Purple)
     * Further clicks = Barriers (Black walls)
   * **Right-click** = Erase a cell.
4. Press keys:

   * **D** → Run **DFS** (Depth First Search)
   * **B** → Run **BFS** (Breadth First Search)
```
---

## 📖 Algorithms

### DFS (Depth First Search)

* Explores as far as possible down one path before backtracking.
* May not find the shortest path.

### BFS (Breadth First Search)

* Explores neighbors level by level.
* Always finds the **shortest path** in an unweighted maze.

---

## 🧮 Time & Space Complexity

* **DFS**:

  * Time Complexity: `O(V + E)`
  * Space Complexity: `O(V)`
* **BFS**:

  * Time Complexity: `O(V + E)`
  * Space Complexity: `O(V)`

---

## ⚡ Requirements

* Python 3
* Pygame library
  Install with:

  ```bash
  pip install pygame
  ```

---
