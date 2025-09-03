import time
import os
from collections import deque

# Maze (0 = path, 1 = wall)
maze = [
    [0,1,0,0,0],
    [0,1,0,1,0],
    [0,0,0,1,0],
    [1,1,0,0,0],
    [0,0,0,1,0]
]

start = (0,0)
goal = (4,4)
rows, cols = len(maze), len(maze[0])
directions = [(1,0),(-1,0),(0,1),(0,-1)]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_maze(path=set(), frontier=[]):
    """Draw maze with ASCII and highlight frontier and path"""
    clear_screen()
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            if (r,c) == start:
                row_str += "S "
            elif (r,c) == goal:
                row_str += "G "
            elif (r,c) in path:
                row_str += "· "   # visited path
            elif (r,c) in frontier:
                row_str += "* "   # frontier (queue/stack)
            elif maze[r][c] == 1:
                row_str += "█ "   # wall
            else:
                row_str += "  "   # empty
        print(row_str)
    print("\n" + "-"*20 + "\n")
    time.sleep(0.5)

def bfs():
    q = deque([(start,[start])])
    visited = set([start])
    while q:
        (x,y), path = q.popleft()
        print("BFS Queue:", [pos for (pos,_) in q])
        print_maze(set(path), [pos for (pos,_) in q])

        if (x,y) == goal:
            return path
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols and maze[nx][ny]==0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                q.append(((nx,ny), path+[(nx,ny)]))
    return None

def dfs():
    stack = [(start,[start])]
    visited = set([start])
    while stack:
        (x,y), path = stack.pop()
        print("DFS Stack:", [pos for (pos,_) in stack])
        print_maze(set(path), [pos for (pos,_) in stack])

        if (x,y) == goal:
            return path
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0<=nx<rows and 0<=ny<cols and maze[nx][ny]==0 and (nx,ny) not in visited:
                visited.add((nx,ny))
                stack.append(((nx,ny), path+[(nx,ny)]))
    return None

# Run simulation
print("🎮 DFS Simulation")
dfs_path = dfs()
print("DFS Path Found:", dfs_path)

time.sleep(2)
print("\n🎮 BFS Simulation")
bfs_path = bfs()
print("BFS Path Found:", bfs_path)
