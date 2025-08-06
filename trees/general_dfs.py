''' Uncategorized problems across Leetcode/Neetcode - DFS (iterative/recursive)

Iterative DFS (stack - last in first out):

def inorder(root):
    res = []
    stack = []
    cur = root
    
    while cur or stack:
        # Find leftmost element
        while cur:
            stack.append(cur)
            cur = cur.left
        # At this point, cur is NULL because it has exited the while loop
        cur = stack.pop() # Pops the most recent element added - essentially the root of any subtree
        res.append(cur)
        cur = cur.right
    
    return res
'''




# Q1
"""
Description - https://leetcode.com/problems/flip-equivalent-binary-trees/description/
Title - Flip equivalent binary tree
Level - Medium
---------------------------------------
Question - 
-> Determine if two given trees are flip equivalent
    -> A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
-> Eg: 

X =         1                Y =        1
        2       3                  3        2
     4    5                              4      5
      
Soln: X,Y will be flip equivalent if we flip the left subtree of X

Thoughts-
-> If mismatch
    -> Check X.right == Y.left
    -> Check X.left == Y.right
-> If not mismatch
    -> Check X.left == Y.left
    -> Check X.right == Y.right
-> Time: O(n)
"""
def flipEquiv(root1,root2) -> bool:

        def dfs(X, Y):
            """
            Compares subtrees that are supposed to be comparable
                - either (left-left and right-right) OR (right-left and left-right)
            """

            # Base cases
            if not X and not Y:
                return True
            if (X and not Y) or (Y and not X) or X.val != Y.val:
                return False
            
            # No flip needed - (left-left and right-right)
            is_flip_needed = (dfs(X.left, Y.left)) and (dfs(X.right, Y.right)) 
            # Check flip equivalence
            is_flip_eq = (dfs(X.left, Y.right)) and (dfs(X.right, Y.left)) 

            return is_flip_needed or is_flip_eq

        
        return dfs(root1,root2) # simple trigger of dfs