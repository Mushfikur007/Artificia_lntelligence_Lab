import random

def generate_grid(N):
   
    grid = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if random.random() < 0.2: 
                grid[i][j] = 1
    return grid

def get_valid_position(grid, N):
   
    while True:
        x, y = random.randint(0, N - 1), random.randint(0, N - 1)
        if grid[x][y] == 0:  
            return (x, y)

def dfs(grid, start, goal, N):
   
    stack = [start]
    parent = {start: None}
    visited = set()
    topological_order = []
    path = []
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        topological_order.append(node)
        
        if node == goal:
            break
        
        x, y = node
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 0 and (nx, ny) not in visited:
                stack.append((nx, ny))
                parent[(nx, ny)] = node
    
    if goal in visited:
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()
    
    return path, topological_order

def print_grid(grid, source, goal, path=None):
   
    N = len(grid)
    for i in range(N):
        for j in range(N):
            if (i, j) == source:
                print("S", end=" ")
            elif (i, j) == goal:
                print("G", end=" ")
            elif path and (i, j) in path:
                print("*", end=" ")  
            else:
                if grid[i][j] == 1:
                    print("#", end=" ") 
                else:
                    print(".", end=" ")  
        print()

def main():
    N = random.randint(4, 7)  
    grid = generate_grid(N)
    source = get_valid_position(grid, N)
    goal = get_valid_position(grid, N)
    
    while source == goal: 
        goal = get_valid_position(grid, N)
    
    path, topological_order = dfs(grid, source, goal, N)
    
    print("Grid:")
    print_grid(grid, source, goal, path)
    print("\nSource:", source)
    print("Goal:", goal)
    
    if path:
        print("\nDFS Path:", path)
    else:
        print("\nNo path found from source to goal.")
    
    print("\nTopological Order of Visited Nodes:", topological_order)

if __name__ == "__main__":
    main()