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



