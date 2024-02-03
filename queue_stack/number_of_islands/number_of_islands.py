from collections import deque

# BFS Solution
def bfs_solution(grid):
    num_of_islands = 0 
    rows, cols = len(grid), len(grid[0])
    def bfs(i, j):
        # Init queue with current row and col
        queue = deque([(i, j)])
        while queue:
            current_row, current_col = queue.popleft()
            if 0 <= current_row < rows and 0 <= current_col < cols and grid[current_row][current_col] == '1':
                grid[current_row][current_col] = '0'
                queue.append((current_row - 1, current_col))  # Up
                queue.append((current_row + 1, current_col))  # Down
                queue.append((current_row, current_col - 1))  # Left
                queue.append((current_row, current_col + 1))  # Right
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                num_of_islands += 1
                bfs(i, j)
    return num_of_islands

# DFS Solution
def dfs_solution(grid):
    num_of_islands = 0 
    rows, cols = len(grid), len(grid[0])
    def dfs(i, j):
        if 0 <= i < rows and 0 <= j < cols and grid[i][j] == '1':
            grid[i][j] == '0' 
        dfs( i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                num_of_islands += 1
                dfs(i, j)
    return num_of_islands