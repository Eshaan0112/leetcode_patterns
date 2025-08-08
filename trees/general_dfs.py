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


# Q2
"""
Description - https://neetcode.io/problems/insert-into-a-binary-search-tree?list=neetcode250
Title - Insert in a BST
Level - Medium
---------------------------------------
Question - 
-> Insert a given node in a BST
-> Eg:          5
            3       9
        1       
        val=6 (to be inserted)
    Soln: Insert to the right of 5 but left of 9

Thoughts - 
-> Brute Force:
    -> Go through each node of the tree, add it to an array, sort the array, add the `val` to the sorted array in the sorted position, rebuild the tree
    -> Time: O(n log n); Space O(n)
-> Optimal:
    -> Make use of the sorting property in a BST (smaller values to the left of a node, larger values to the right of the node)
    -> Take the above eg, we check if 6 < or > the root, 5 and DFS to the right (since 6>5), then we DFS in a similar manner till we reach the left of 9 and add the value 6 and return
    -> The thing to note here is the return value of the DFS. Say we are at dfs(9) function call:
        -> We check 6 < 9 so we now need to dfs(9.left) i.e dfs(none)
        -> If we reach a none node that means we need to add a node with `val`, so we build a node(val=6) here
        -> We must return the node that's been created and assign it to the correct position (i.e the position it was dfs-ed from which was to the left of 9)
        -> So finally, something like:
            node.left = dfs(node.left) where the return value of dfs is the value that was added
        -> ** For any other node, this way where we do node = dfs(node), it propagates up the tree/graph with the value at the dfs position
    -> Time: O(h), h=height of tree since at each height level, we have 1 comparison
""" 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(root,val):

        def dfs(node):
            """
            If val<node -> go left
            If val>node -> go right
            
            The main idea to keep in mind here is that we propagate back up the same node that's traversed, so the links
            between the tree nodes are maintained.
            """

            nonlocal val # to make sure the nested function reads the outer function's val

            if not node: return TreeNode(val)

            # Search
            if val < node.val:
                node.left = dfs(node.left)
            elif val > node.val:     
                node.right = dfs(node.right) 
            return node          
        
        root = dfs(root) # trigger
        return root


# Q2
"""
Description - https://neetcode.io/problems/binary-tree-right-side-view?list=neetcode250
Title - Binary tree right side view
Level - Medium
---------------------------------------
Question - 
-> Return elements that can be viewed from the right
-> Eg1:                         1
                        2               3
                    4       5         6
        soln: [1,3,6]
-> Eg2:
                                1
                        2
                    5       3
        soln: [1,2,3]

Thoughts -
-> We want to view the tree only from the right side. Ideally we want to return elements that are the right-most
-> In a DFS approach, we can think of simply just traversing to the right of each node, but what if we get an example like Eg2 above.
    -> There are no nodes to the right of 1, so we can't JUST traverse right
    -> We must traverse right first (if there is an element there, we add it)
    -> Then we traverse left - if there is not element to the right, then we add element to the left
-> How do we know which element to add? We must add the very first element during our DFS we see.
    -> This way, we'll guarantee to add the right-most element as we traverse the right subtree first
-> Time: O(h) --> add 1 element per depth    
"""
def rightSideView(root):
    res = []
    
    def dfs(node, level):
        """ DFS with priority to the right and add first(rightmost) element per level """
        if not node: return None 

        # If this node is the first at the current level, add it
        if level == len(res): # we'll be able to see only one element per level from the right
            res.append(node.val)
        
        # Try to find element to the right first
        dfs(node.right, level+1)
        dfs(node.left, level+1)

    dfs(root,level=0) # need to pass in level to idenitfy which is the first element at that level we are seeing

    return res

