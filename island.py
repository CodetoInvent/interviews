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
    



# leetcode

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return main(grid)
        
def main(grid):
    if not grid or not grid[0]: return 0
    
    visited = set()
    island_number = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if search(row, column, grid, visited):
                island_number +=1
    
    return island_number
                    
def search(row, column, grid, visited):    
    if grid[row][column] != '1': return False
    if (row, column) in visited: 
        return False
    
    in_bounds = lambda x, y: (x >= 0 and x < len(grid)) and (y >= 0 and y < len(grid[0]))
    stack = [(row, column)]
    
    while stack:
        top = stack.pop()
        row, column = top
        if top in visited \
            or not in_bounds(row, column) \
            or grid[row][column] != '1': 
            continue
        visited.add((row, column))
        
        stack.append((row-1, column)) 
        stack.append((row+1, column))
        stack.append((row, column-1)) 
        stack.append((row, column+1))
    return True
        