''' Topological sorting questions from Neetcode/Leetcode - 

Use Cases:
    -> Only works for DAGs
    -> Find a linear ordering in which some given tasks need to be performed in an order

Definition:
    -> Topological sorting of a directed acyclic graph is nothing but the linear ordering of vertices such that if there is an edge between node u and v(u -> v), node u appears before v in that ordering.

Kahn's algorithm (if Topological sort is done using BFS)
    Approach:
    -> Uses BFS (queue)
    -> Steps of algorithm:
        Step 1: Add all nodes with in-degree 0 to queue
        Step 2: While queue is not empty:
                2a: Remove a node from the queue
                2b: For each outgoing edge from the removed node:
                    2b1: Decremement the in-degree of the destination node by 1
                    2b2: If the in-degree of the destination node becomes 0, add it to the queue
        Step3: If queue is empty and there are still nodes in the graph, the graph is NOT a DAG as it contains a cycle
        Step4: The nodes in the graph represent the topological order of the graph

Topological sort using DFS
    tbd
'''

# Q1
"""
Description - https://neetcode.io/problems/course-schedule?list=neetcode150
Title - Course Schedule
Level - Medium
---------------------------------------
Question - 
-> Given prerequistes, determine if all courses can be completed
-> Eg: 
input: numCourses = 2, prerequisites = [[0,1]]
Soln: True (First take course 1 (no prerequisites) and then take course 0)


Thoughts - 
-> Since we have prerequisties, the courses will have to be taken in some sort of order. Think Topological sorting here.
-> Time: O(V+E) --> Simple BFS
"""

def canFinish(numCourses, prerequisites):
        # Setup
        indegree = [0] * numCourses # nodes and their indegrees; node numbering is based on the index.
        adj = [[] for i in range(numCourses)] # adjacency list of all nodes

        '''
        for a prerequisite input [a,b] => b is the prerequisite to a i.e graph looks like a-->b where indegree of b is 1
        '''
        for course, prereq in prerequisites:
            indegree[prereq] += 1 
            adj[course].append(prereq) # for [a,b], b is a neighbor of a

        # Kahn's topological sort

        # Step 1: Add all nodes with in-degree 0 to queue 
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        ''' Step 2: While queue is not empty:
                2a: Remove a node from the queue
                2b: For each outgoing edge from the removed node:
                    2b1: Decremement the in-degree of the destination(in our case, the prereq) node by 1
                    2b2: If the in-degree of the destination node becomes 0, add it to the queue'''
        
        courses_able_to_complete = 0
        while q:
            course = q.popleft()
            courses_able_to_complete += 1
            for neighbor in adj[course]: # course -> neighbor
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # Step3: If queue is empty and there are still nodes in the graph, the graph is NOT a DAG as it contains a cycle
        return courses_able_to_complete == numCourses
    
# Q2
"""
Description - https://neetcode.io/problems/course-schedule-iv?list=neetcode250
Title - Course Schedule IV
Level - Medium
---------------------------------------
Question - 
-> Read from description
-> Eg : numCourses = 4; prerequisites: [[1,0],[2,1],[3,2]]; queries: [[0,1],[3,1]]
    Soln: [false, true]

Thoughts - 
-> In this, prerequisites can be indirect i.e if course 0 is a prereq of course 1 and 1 a prereq to 2, then 0 is a prereq to 2
-> The idea is to identify in `queries`[u,v] whether u is a prereq to v
-> Brute Force:
    -> We can simply build the graph first
    -> Using the above eg (since [a,b] means a before b)
        3 --> 2 --> 1 --> 0
        -> In queries: [[0,1],[3,1]],
            -> For [[0,1]], 0 is the prereq and 1 is the course, so if we start at 0 to try and find 1 (using DFS), we won't be able to. Hence return False
            -> For [[3,2]], we start at 3 and can reach 1 by DFS-ing
    -> Time Complexity: O(Q * n) where Q=number of queries, n=Number of Nodes since we do a DFS for each of the courses in queries

-> Optimal:
    -> If we somehow have a list of prerequisites for each course (including indirect ones), we can reduce our time complexity by not having to DFS till we can't anymore
    -> The game here would be in what to return when we propagate up in the DFS
        -> Let's take the 3-->2-->1-->0 eg:
            -> Here prereqs to 0 are (3,2,1)
            -> With the way our graph is built, the edge is going from prereq -> course, but it'll be easier if we do the opposite i.e go from course to prereq
                -> New graph 0-->1-->2-->3
                    -> The prereqs to course 0 are: (1,2,3) and 3 has no prereqs
            -> Let's say we have a map that maps 0:(1,2,3) 1:(2,3) 2:(3) 3:(), we can easily just simply do a lookup to answer the queries
    -> How to build the map?:
        -> Build the adjacency list and DFS for each course and when we return we return a set of prereqs for the node we are returning from
        -> 0        -dfs--> 1          -dfs-->          2 -dfs-->      3
        0:(1,2,3)               return (1,2,3)        return(2,3)    return (3)
        
    -> Time Complexity: O(Q + (V+E)n), Q = Number of queries (just a simple O(1) lookup); (V+E)*n: Here (V+E) is the time to do DFS traversal
        and for each dfs traversal we do, we propagate the union of sets. Time complexity for merging of sets at a node is n and we do this for every dfs traversal
"""   

def checkIfPrerequisite(numCourses, prerequisites,queries):
        
        # Build graph
        adj = [[] for _ in range(numCourses)]
        for prereq, course in prerequisites:
            adj[course].append(prereq)
        
        def dfs(course):
            """ 
            -> DFS from each course, add prerequistes and use propagate up values to add indirect prerequisites
            -> Propagates up the added prerequiste set
                -> if a-->b-->c-->d then, d will return d, c will return (c,d), b will return (b,c,d) 
            """
            
            if course not in prereq_map:
                prereq_map[course] = set() # set of prereqs and indirect prereqs

                # DFS
                for prereq in adj[course]:
                    prereq_map[course] |= dfs(prereq) # |= union of sets; say we're at b in the above eg: this will union return value of c with already exisiting value d so return value of b becomes (c,d)
                prereq_map[course].add(course) # referring to above eg, we also need to add the course itself, so if we're at b it should return b and (c,d)
            
            return prereq_map[course]
        
        
        prereq_map = {} # course: (prereq, indirect prereqs)

        # Fill in the prereq map for each course using "propragate up" values of dfs
        for course in range(numCourses):
            dfs(course)
        
        # Check queries
        res = []
        for u,v in queries:
            if u in prereq_map[v]:
                res.append(True)
            else:
                res.append(False)
        
        return res
        
    

