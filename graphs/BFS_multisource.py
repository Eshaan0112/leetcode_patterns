''' Multisource BFS problems from Neetcode 150 
Used in problems that need to find "nearest distance" or "minimums" 
'''

# Q1
"""
Description - https://neetcode.io/problems/islands-and-treasure?list=neetcode150
Title - Island and Treasure List
Level - Medium
---------------------------------------
Question - 
-> We want to fill each land cell with the distance to its nearest treasure chest and modify the given grid in place
-> Eg:

    
        INPUT:  [[INF,-1,0,INF],
                [INF,INF,INF,-1],
                [INF,-1,INF,-1],      
                [0,-1,INF,INF]]
        
        
        Soln:   [3,-1,0,1],
                [2,2,1,-1],
                [1,-1,2,-1],
                [0,-1,3,4]

Thoughts -
-> Brute Force: 
    -> DFS from each land cell (INF) to all possible treasure chests(0) and take the smallest distance out of all traversals
    -> Time: O(m*n * 4^(m*n))

-> Optimal
    -> Since we need to calculate the distance to the "nearest" treasure chest, think BFS 
        -> First option is to try BFS starting from the land cells (SPOILER: this doesn't work!)
            -> In this option, let's dry run the given eg:
                [[INF,-1,0,INF],               
                [INF,INF,INF,-1],           
                [INF,-1,INF,-1],      
                [0,-1,INF,INF]]
                
                [[1,-1,0,INF],               
                [start_bfs,1,INF,-1],           
                [1,-1,INF,-1],      
                [0,-1,INF,INF]]
                
                let's say we are at (r,c)=(1,0), our queue for BFS would be positions (0,0); (1,1); (2,0)
                -> The distance from our start i.e (1,0) would be (0,0): 1 ; (1,1): 1 ; (2,0) : 1
                -> Now see that at the position (0,0) cannot be updated anymore, so we are saying the distance to the nearest treasure chest is 1 for land cell at position (0,0)
                -> However, this result is wrong as the nearest treasure chest is at position (3,0) so the distance at position (0,0) should be 3
       
        -> Second option is to reverse our thinking and start BFS from treasure chest (NOT OPTIMAL BUT WORKS)
            -> In this option, let's dry run the same eg:
                [[INF,-1,0,INF],               
                [INF,INF,INF,-1],           
                [INF,-1,INF,-1],      
                [0,-1,INF,INF]]
                
                let's say we start at our treasure chest at (r,c) = (0,2) and do BFS. At some point our grid would look like this (considering we are still at the BFS loop for the start position of (0,2))
                [[4,-1,0,1],               
                [3,2,1,-1],           
                [4,-1,INF,-1],      
                [0,-1,INF,INF]]
                
                but you can see that the distance at position (r,c) = (0,0) is not the "nearest" yet. We will have to essentially BFS from all treasure chests and update the smallest distance if seen for every BFS start
                -> This gives us a time complexity of O((m*n)^2)
        
        -> Third option is to continue with our reverse thinking and start multi-source BFS
            -> We can think about this as doing BFS from all treasure chests in parallel
            -> We mark the positions we want to start our BFS from (i.e all treasure chests) and do all BFS traversals simulataneously
            -> Time: O(m*n) -> only need to see each element in the grid once
"""

def islandsAndTreasure(grid):
        
        # Setup
        water, treasure, land = -1,0,2147483647
        ROWS,COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set() # to keep track of visited elements in the grid. We don't need to worry about nearest distance with this method

        # Mark start of multisource BFS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == treasure:
                    queue.append([r,c]) # add sources for multisource BFS
                    visit.add((r,c))
        
        def branch(r,c):
            """
            Visits elements in the same level for BFS and adds them to a queue
            """
            # Exit conditions
            if r == ROWS or c == COLS or r<0 or c<0 or grid[r][c] == water or (r,c) in visit:
                return
            
            visit.add((r,c))
            queue.append([r,c])
            

        distance = 0 # distance from treasure cell to treasure cell is obviously 0

        # Branch outward from sources and add distances to every land encountered
        while queue:
            for _ in range(len(queue)) : # for each source in multisource BFS - doing BFS traversal in "parallel"
                r,c = queue.popleft()
                grid[r][c] = distance # add "nearest" distance
                
                # Branch outward - next level
                branch(r+1,c) # Up level
                branch(r-1,c) # Down level
                branch(r,c+1) # Right level
                branch(r,c-1) # Left level

            distance += 1 # increment after each level as the nearest distance
            

# Q2
"""
Description - https://neetcode.io/problems/islands-and-treasure?list=neetcode150
Title - Rotten Oranges
Level - Medium
---------------------------------------
Question - 
-> Very similar to Q1
-> An extra variable is needed to keep track of how many fresh fruits there so at the end we can check whether it is possible to traverse all fresh fruits or not

Thoughts-
-> Multisource BFS is optimal. Can do DFS as well, but the time complexity would be O(m*n*4^(m*n))
-> Time: O(m*n)
"""
def orangesRotting(grid):
        # Setup
        fresh = 1
        empty = 0
        rotten = 2
        queue = deque() 
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh_count = 0 # number of fresh fruits to be made rotten - this is to check if it's possible to visit every fresh fruit in the grid from any rotten fruit

        # Count fresh fruits and add rotten fruits as source for multisource BFS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == fresh: 
                    fresh_count += 1
                elif grid[r][c] == rotten:
                    queue.append([r,c])
        
        def branch(r,c):
            nonlocal fresh_count
            # Exit conditions
            if r==ROWS or c==COLS or r<0 or c<0 or grid[r][c] == empty:
                return 
            
            # Make fresh fruits rotten and traverse that level
            if grid[r][c] == fresh: 
                queue.append([r,c])
                grid[r][c] = rotten
                fresh_count -=1 # fresh fruit converted to rotten

            
        minimum_time = 0
        while fresh_count and queue:
            for level in range(len(queue)):
                r,c = queue.popleft()

                # branch outward in up/down/left/right directions
                branch(r+1,c)
                branch(r-1,c)
                branch(r,c+1)
                branch(r,c-1)
            minimum_time+=1
        
        # If at the end, no fresh fruits remain, we have successfully traversed all fresh fruits
        return minimum_time if fresh_count == 0 else -1