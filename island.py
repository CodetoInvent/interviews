from collections import deque

def find_region(grid, column, row):
    queue = deque()
    queue.append((column, row))
    
    count = 0
    while queue:
        c, r = queue.popleft()
        
        out_of_bounds = (c < 0 or c >= len(grid)) or (r < 0 or r >= len(grid[0]))
        if out_of_bounds or grid[c][r] == 0: continue
        grid[c][r] = 0
        count += 1
        
        queue.append((c, r-1))
        queue.append((c, r+1))
        queue.append((c-1, r))
        queue.append((c+1, r))
        queue.append((c-1, r-1))
        queue.append((c+1, r+1))
        queue.append((c+1, r-1))
        queue.append((c-1, r+1))

    return count

def find_region_recursive(grid, c, r):
    count = 0
    if c == len(grid) or r == len(grid[0]): return count
    if c < 0 or r < 0: return count
    if grid[c][r] != 1: return count
    grid[c][r] = 0
    count += 1
    count += find_region_recursive(grid, c, r-1)
    count += find_region_recursive(grid, c, r+1)
    count += find_region_recursive(grid, c-1, r)
    count += find_region_recursive(grid, c+1, r)
    count += find_region_recursive(grid, c-1, r-1)
    count += find_region_recursive(grid, c+1, r+1)
    count += find_region_recursive(grid, c+1, r-1)
    count += find_region_recursive(grid, c-1, r+1)
    
    return count
        

def get_biggest_region(grid):
    if not grid: return 0
    
    maximum = 0
    for column in range(len(grid)):
        for row in range(len(grid[0])):
            if grid[column][row] == 1:
                count = find_region_recursive(grid, column, row)
                maximum = max(maximum, count)
    
    return maximum
    