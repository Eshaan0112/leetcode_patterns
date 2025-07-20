''' Root to leaf from Leetcode '''

# Q1
"""
Description - https://leetcode.com/problems/binary-tree-paths/
Title - Root to leaf
Level - Easy
---------------------------------------
Question - 
-> Return all root to leaf paths in a tree
-> Eg:                  1
                    2       3
                        5
                    Soln: ["1->2->5", "1->3]
                    
Thoughts - 
-> DFS traversal (a stack can be used or recursion)
-> Time: O(n) --> visiting each node once
"""

def tree_path(root):
    ''' Iterative DFS using a stack (Last in First out) '''
    """res = []
    if not root: return res # edge case
    
    # DFS
    stack = [(root, str(root.val))]
    
    while stack:
        node,path = stack.pop() # pop last added node
        
        if not node.left and not node.right: # Leaf node -> add complete path
            res.append(path)
        if node.right:
            # add right side path: 1->3
            stack.append((node.right, path + "->" + str(node.right.val))) 
        if node.left:
            # add left side path: 1->2
            stack.append((node.left,path + "->" + str(node.right.val)))
    
    return res"""
    
    ''' Recursive DFS '''
    res = []
    def dfs(node,path):
        """ 
        Goes through the left path, then the right path of the tree
        node = node being visited; 
        path = path preceding node being visited 
        """
        if not node: return # edge case
        
        if not node.left and not node.right:
            res.append(path+str(node.val)) # add leaf node value to existing path
            return
        else:
            path += str(node.val) + "->" # "1->""; L-- "1->2->"; L-- "1->2->5"; R-- "1->3->"
            dfs(node.left, path)
            dfs(node.right, path)
    
    dfs(root, "")
    return res
    
    
            
            