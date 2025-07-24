''' Graph problems from Neetcode 150

DFS approach for grid traversal(recursive or iterative stack)
    def solution(grid):
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r,c):
            # Base Case - exit conditions -> Valid for traversal of 2D grid problems
            if r==ROWS or c==COLS or (r,c) in visited or r<0 or c<0 or any_other_condition:
                return __
            
            # Visit grid[r][c]
            visit.add((r,c))
            
            # Other operations as needed
        
            return x -> think of the return value of DFS to be something you want to propagate back to the previous dfs call. Could be None.
        # call dfs
    
    -> May need a "visit" set to keep track of visited elements

BFS approach (deque) i.e First In First Out (FIFO)
    def solution:
        q = deque([start])
        while q:
            first_out = q.popleft() # popleft removes the first element that was added
            # Other operations as needed
'''

# Q1
"""
Description - https://neetcode.io/problems/count-number-of-islands?list=neetcode150
Title - Number of Islands
Level - Medium
---------------------------------------
Question - 
    -> Given a grid of "1" (land), "0" (water), find number of islands

Thoughts - 
    -> We want to find adjacent "1"s to every "1" till we can't anymore. Any "1" that's connected to another "1" is part of the same island
    -> Points to DFS on every element of the given grid
    -> Time: O(m*n * 4^(m*n)) - m*n is the size of the grid and we are calling DFS on every element of the grid 4 times (up/down, left/right)
"""
def numIslands(grid):
        # Setup
        land,water = "1","0"
        ROWS,COLS = len(grid), len(grid[0])
        visited = set() # keep track of positions that have been visited
        islands = 0

        def dfs(r,c):
            """
            Visit 4 directional elements for each land mass in the given grid
            """
            # Base case for DFS - exit conditions possible when DFS-ing
            if r==ROWS or c==COLS or (r,c) in visited or grid[r][c]==water or r<0 or c<0:
                return 
            
            # 4 directional DFS
            visited.add((r,c)) # currently visiting grid[r][c]
            dfs(r+1,c) # up
            dfs(r-1,c) # down
            dfs(r,c+1) # right
            dfs(r,c-1) # left

            return

        # DFS for every land we encounter
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == land and (r,c) not in visited: # if we've already visited the land mass, we don't need to DFS from it
                    dfs(r,c)
                    islands += 1 # increment this only when DFS for each position is returned
        
        return islands

# Q2
"""
Description - https://neetcode.io/problems/max-area-of-island?list=neetcode150
Title - Max Area of islands
Level - Medium
---------------------------------------
"""
class Solution:
    def maxAreaOfIsland(grid):
        """
        WHY THIS DOESN'T WORK (python specific):
        1. We do:
            area = 0
            area += dfs(..area) # call 1 (say area returned=2)
            area += dfs(..area) # call 2 (here area as argument to dfs will not be 2 but 0, so this "update" functionality doesn't work since area is an int and ints are immutable in python). You are simply just passing in a local copy of are and not a reference. 
        2. Alt:
            return 1 + dfs(..) + dfs(..) +... in DFS function
        """

        # Setup
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        land = 1
        water = 0
        maxArea = 0

        def dfs(r,c,area): # don't need "area" as an arg here
            # Base Case - exit conditions
            if r==ROWS or c==COLS or (r,c) in visited or grid[r][c] == water or r<0 or c<0:
                return 0 # we want to propagate the area of 0 back to the previous (r,c) position
            
            visited.add((r,c)) # currently visiting grid[r][c]

            # DFS in 4 directions and accumulate area for island  -DOESN'T WORK
            '''area += dfs(r+1,c, area)
            area += dfs(r-1,c, area)
            area += dfs(r,c+1, area)
            area += dfs(r,c-1, area)
            return 1+area # increment area as land is encountered for each position (r,c)'''
            
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1) # this works
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == land and (r,c) not in visited:
                    area = dfs(r,c,area=0) # don't need to pass in area as an arg here..area = dfs(r,c) will suffice
                    maxArea = max(maxArea, area)
        return maxArea




