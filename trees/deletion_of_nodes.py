''' Deletion of nodes in Tree from Leetcode

Basic Idea of deleting nodes in a Tree:
1. Tree traversal is generally DFS
2. In DFS, we need there are two phases - top down (when you are going towards the leaf) and b
bottom up (when you are propagating up from the leaf to the root i.e returning from DFS function)
3. To delete a particular node, the trick is simple - return None when propagating from a node that is to be deleted. For eg:
    node_to_deleted.left = dfs() and within this dfs() have functionality to return None if node is to be deleted.
4. If a node is not to be deleted then return its own value (proagate it up)

Essentially:
def DFS(node):
    if node to be deleted:
        return None
    else:
        return node
'''

# Q1
"""
Description - https://leetcode.com/problems/delete-nodes-and-return-forest/
Title - Delete Nodes and Collect Forests
Level - Medium

---------------------------------------
Question - 
-> Delete given nodes and return the roots of trees that are left after deletion

Thoughts - 
-> Follow the approach to delete nodes in the tree
-> The candidate roots of the forest will be children of the nodes that have been deleted
-> We maintain a set such that we can maintain candidate roots and add and delete them based on which nodes are to be deleted
-> Time: O(n) --> Visit each node at most once
"""

def delNodes(root, to_delete):

        # Setup
        forest_roots = set([root]) # candidate roots of the forest
        to_delete = set(to_delete) # convert given list to set for O(1) lookup time

        def dfs(node):
            """
            Deletes given nodes and collects candidate roots as DFSed
            """

            if not node: return None # base case

            propagate_value = node # propagate value = node value itself if not to be deleted
            
            if node.val in to_delete: 
                forest_roots.discard(node) # it's possible the node to be deleted was added in a previous step as a candidate root
                # Add children of deleted node as candidate roots
                if node.left: forest_roots.add(node.left)
                if node.right: forest_roots.add(node.right)
                propagate_value = None # propagate value = NULL if node to be deleted

            node.left = dfs(node.left)
            node.right = dfs(node.right)
            return propagate_value

        _ = dfs(root) # start dfs
        return list(forest_roots)

# Q1
"""
Description - https://neetcode.io/problems/delete-node-in-a-bst?list=neetcode250
Title - Delete Node in a BST
Level - Medium
---------------------------------------
Question - 
-> Delete a node with a given value in a BST

Thoughts - 
-> Read comments below
-> Time: O(h)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):
        if not root: return root # base case
        
        # Search for key
        if key < root.val :
            root.left = self.deleteNode(root.left, key) # assign node = dfs(node) to return updated tree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else: # key found
            # If at this position there is no left node of the key, we can simply return the right subtree of the node
            if not root.left: return root.right

            # Vice-Versa
            if not root.right: return root.left

            '''
            If both left and right subtrees of the node to be deleted exist, we need to assign the minimum of right subtree as the "propagate up" value to maintain the BST properties
            Check this example: key=2
                    8                               8
                2       9       --soln-->       3       9   
            1       4                         1   4   
                  3   5                             5 

            Here when we're deleting node 2, the "propagate up" value is node 3 (which is the minimum of the right subtree of 2)
            Since we're finding the minimum value of the right subtree, it is guaranteed that the left subtree of the key node will be
            less than the new "propagate up" value (1<min(right subtree of 2) = 1<3) and the rest of the values will be greater (4 and 5 > 3)
            '''
            # Find minimum of the right subtree and replace its value for the key node to be deleted
            cur = root.right
            
            while cur.left:
                cur = cur.left
            minimum_of_right_subtree = cur.val
            root.val = minimum_of_right_subtree

            # At this point, the tree will look like this:
            '''
                                8
                            3       9
                        1      4
                              3   5
            We can see that even though we've replaced the node to be deleted, we are left to delete it from the position it was taken from, so we
            need to recursively delete that one as well
            '''
            root.right = self.deleteNode(root.right,minimum_of_right_subtree) 

        return root
