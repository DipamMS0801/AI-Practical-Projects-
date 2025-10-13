import heapq
import matplotlib.pyplot as plt
import numpy as np

# ---- A* Algorithm Implementation ----
def heuristic(a, b):
    """Heuristic: Manhattan distance"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    """Finds the shortest path from start to goal using A*"""
    rows, cols = grid.shape
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        x, y = current
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            neighbor = (x + dx, y + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor] == 0:
                tentative_g = g_score[current] + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None  # No path found


# ---- Visualization ----
def plot_grid(grid, start, goal, path=None):
    plt.figure(figsize=(6,6))
    plt.imshow(grid, cmap='Greys', origin='upper')
    plt.scatter(start[1], start[0], marker='o', color='green', s=150, label='Start')
    plt.scatter(goal[1], goal[0], marker='X', color='red', s=150, label='Goal')
    
    if path:
        px, py = zip(*path)
        plt.plot(py, px, color='blue', linewidth=2, label='Path')
    
    plt.legend()
    plt.title("A* Pathfinding Visualization")
    plt.axis('off')
    plt.show()


# ---- Main Program ----
if __name__ == "__main__":
    # 0 = free cell, 1 = obstacle
    grid = np.array([
        [0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ])
    
    start = (0, 0)
    goal = (4, 5)
    
    path = astar(grid, start, goal)
    
    if path:
        print("Shortest Path Found:")
        print(path)
    else:
        print("No Path Found!")
    
    plot_grid(grid, start, goal, path)
