''' DFS problems from Neetcode 150

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
Question - 
-> Calculate max area across a grid 

Thoughts - 
-> Similar to Q1, just need to calculate area of each island to see which one is max
-> Time: O(m*n*4^(m*n))
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

# Q3
"""
Description - https://neetcode.io/problems/clone-graph?list=neetcode150
Title - Clone Graph
Level - Medium
---------------------------------------
Question - 
-> Create a deep copy of every node in a given graph
-> Eg:
    INPUT: [[2],[1,3],[2]] => Node1:(1,[2]) Node2:(2,[1,3]), Node3: (3,[2])
    SOLN: [[2],[1,3],[2]]

Thoughts -
-> DFS on each node and create nodes as encountered
-> To make sure we don't creat multiple copies of the same node (if a node is a neighbor of 2 or more nodes), once we create a node, we keep track of it
-> Time: O(n), n = V+E where V=vertices, E=edges
"""

def cloneGraph(node):
        """
        Given:
        class Node:
            def __init__(self, val = 0, neighbors = None):
                self.val = val
                self.neighbors = neighbors if neighbors is not None else []
        """

        # Setup
        mapping_of_nodes = {} # {given_node: created_node} to keep track of which nodes have been created
        deep_copied_graph = None # if given node is None, then we can just return this

        def dfs(node):
            """
            Visit each node's neighbors and create them if they have not already been created.

            """
            if node in mapping_of_nodes: # node already created
                return mapping_of_nodes[node] # return the created nodes; mostly these will be created neighbors
                
            # Create a deep copy and add to mapping
            deep_node = Node(node.val) # create a new node with the needed value
            mapping_of_nodes[node] = deep_node

            # Create the current node's. We return before if the node has already been created
            for neighbor in node.neighbors: # neighbors of each copied node. Neighbors are also nodes so we run dfs to create the neighbors
                created_neighbors = dfs(neighbor)
                deep_node.neighbors.append(created_neighbors) # append to the 'neighbors' list as part of the Node object
            
            return deep_node
            
        if node is not None:
            deep_copied_graph = dfs(node)

        return deep_copied_graph

# Q3
"""
Description - https://neetcode.io/problems/pacific-atlantic-water-flow?list=neetcode150
Title - Pacific Atlantic Water Flow
Level - Medium
---------------------------------------
Question - 
-> Find elements in a grid that can reach pacific and atlantic, where pacific is top row and left column and atlantic is bottom row and right column
-> We can traverse to another element if it is less than or equal to current element
-> Eg:                 pppppppp 
            p        [[4,2,7,3,4],a
            p        [7,4,6,4,7], a
            p        [6,3,5,3,6]] a
                      aaaaaaaaa

Soln: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Thoughts - 
-> Brute Force:
    -> We can DFS starting from each element and check if it is going to pacific and atlantic
    -> Time: O(m*n*4^(m*n))

-> Optimal:
    -> Elements in the first row and first column are adjacent to pacific ocean, so they can automatically reach it. 
    -> Similarly for last row and last column (they're adjacent to atlantic)
    -> What if, instead of going from each element in the grid, we reverse our thinking and find elements from the first row and first column that are traversible and do the same thing for last row and last column
    -> This would allow us to find elements that reach atlantic from pacific and pacific from atlantic. The intersection of these elements can reach both.
    -> NOTE: When we reverse our thinking - i.e go from ocean boundary to elements instead of elements to ocean boundary, the condition for traversal would also be reversed. 
        -> Given condition was that we can traverse if the next element is <= current element (from element to ocean boundary) but now
            next element must be >= current element
    -> Time: O(m*n) --> visit each element once
"""

def pacificAtlantic(heights):

        # Setup
        ROWS, COLS = len(heights), len(heights[0])
        pacific_visit, atlantic_visit = set(),set() # to keep track of elements that have been visited 
        res = []

        def dfs(r,c,visit,prev_height):
            """
            Visits elements from Pacific that can reach Atlantic and vice-versa.

            Args:
            prev_height maintains the height of the previous element to check whether traversal is possible. Starting value of
            prev_height is itself since we search >= (opposite condition)
            """

            # Exit conditions
            if r==ROWS or c==COLS or (r,c) in visit or r<0 or c<0 or heights[r][c] < prev_height:
                return
            
            visit.add((r,c)) # currently traversing (r,c)

            # 4 directional traversal
            dfs(r+1,c,visit, prev_height=heights[r][c]) # up
            dfs(r-1,c,visit, prev_height=heights[r][c]) # down
            dfs(r,c+1,visit, prev_height=heights[r][c]) # left
            dfs(r,c-1,visit, prev_height=heights[r][c]) # right
            
        # First row elements can reach pacific (0,c) and last row (ROWS-1,c) can reach atlantic
        for c in range(COLS):
           dfs(0,c, pacific_visit,prev_height=heights[0][c]) 
           dfs(ROWS-1, c, atlantic_visit, prev_height=heights[ROWS-1][c])

        # Last row elements can reach atlantic (r,0) and last column elements (COLS-1,c) can reach pacific
        for r in range(ROWS):
            dfs(r, 0, pacific_visit, heights[r][0])
            dfs(r, COLS - 1, atlantic_visit, heights[r][COLS - 1])
        
        '''
        At this point, we've added elements that can be reached from pacific->atlantic to pacific_visit set
        and elements that can be reached from atlantic->pacific to atlantic_visit set. The elements that intersect between
        the two sets are our solution
        '''
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific_visit and (r,c) in atlantic_visit:
                    res.append([r,c])
        
        return res

# Q4
"""
Description - https://neetcode.io/problems/surrounded-regions?list=neetcode250
Title - Surrounded Regions
Level - Medium
---------------------------------------
Question - 
-> Mark all surrounded regions of "O"s as "X"s
-> The border "O"s (and connected "O"s to the border "O"s) are considered unsurrounded
-> Eg:

Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]

Soln: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]

Thoughts - 
-> Brute Force:
    -> Identify all surrounding regions and unsurrounded regions using DFS
    -> Then change the surrounding regions to "X"s
    -> This will take O(m*n) memory and O(m*n * 4^m*n) time

-> Optimal:
    -> Reverse thinking: Instead of getting surrounded regions, think of capturing everything but unsurrounded regions that are "O"s
    Step1: Find all "O"s and their connected "O"s that are at the borders and mark them as "T" (to identify that these are unsurrounded)
    Step2: Change every "O" that's left since every "O" that's left will be surrounded for sure
    -> Time: O(m*n) --> visit every element once
    """

def solve(board):
        # Setup
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()

        def dfs(r,c):
            # Exit conditions
            if r == ROWS or c == COLS or r<0 or c<0 or (r,c) in visit or board[r][c] == "X":
                return
            
            visit.add((r,c))
            board[r][c] = "T"

            # 4 directional traversal
            dfs(r+1,c) # Up
            dfs(r-1,c) # Down
            dfs(r,c+1) # Right
            dfs(r,c-1) # Left


        # Mark Border "Os"
        
        # Top and Bottom border
        for c in range(COLS):
            if board[0][c] == "O":
                dfs(0,c)
            if board[ROWS-1][c] == "O":
                dfs(ROWS-1,c)

        # Right and Left border
        for r in range(ROWS):
            if board[r][0]:
                dfs(r,0)
            if board[r][COLS-1]:
                dfs(r,COLS-1)
        
        # Change remaining "Os" in the board as "X" as we have marked "Os" that are unsurrounded with "T"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Every surrounded region has been changed to X, but the "T"s we had put for unsurrounded region remains.
        # We need to change them back to Os
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
