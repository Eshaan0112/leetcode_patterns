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

