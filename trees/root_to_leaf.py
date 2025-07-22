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

''' Path Sum Questions '''
# Q2
"""
Description - https://leetcode.com/problems/path-sum/
Title - Path Sum
Level - Easy
---------------------------------------
Question - 
-> Return true if a root-to-leaf path exists such that adding up all values along the path equals a given, targetSum
-> Eg: targetSum = 7
            1
        2       3
    4       6
    Soln: True (1->2->4 = 1 + 2 + 4 == 7)

Thoughts -
-> Visit each node and at whenever the path reaches a leaf, check the sum of the path (including current node). If it is == targetSum, the return value would be True, else keep looking
-> Time: O(n) --> Visiting each node once
"""

class Solution:
    def hasPathSum(self, root,targetSum):
        res = False

        def dfs(node, path):
            """
            Visits each node
            """
            nonlocal res # to see the value once amongst both functions

            # Base Cases
            if not node: return 

            if not node.left and not node.right:
                if sum(path)+node.val == targetSum:
                    res = True
                    return 
            else:
                # Here we dfs using path that doesn't include the node we want to explore - it only includes nodes from root->parent
                path.append(node.val) # add node to explore paths with that node
                dfs(node.left, path)
                dfs(node.right, path)
                path.pop() # remove node once path with that node explored --> dry run through this eg: root = [1,-2,-3,1,3,-2,null,-1] to understand

        dfs(root,[])
        return res
                   

# Q3
"""
Description - https://leetcode.com/problems/path-sum-ii/
Title - Path Sum 2
Level - Medium
---------------------------------------
Question -       
-> Add all paths from root to leaf that add up to a given sum

Thoughts - 
-> Very similar to PathSum
"""   
def pathSum(self, root, targetSum):
        paths = []
        
        def dfs(node, curr_path):
            """ Visit each node """
            
            if not node: return

            if not node.left and not node.right:
                if sum(curr_path) + node.val == targetSum:
                    curr_path.append(node.val)                    
                    paths.append(curr_path.copy()) # if .copy is not used, we end up appending a reference to curr_path to paths, which will make changes as we change curr_path. So, we need to append a snapshot of it using .copy()
                    curr_path.pop() # need to make sure curr_path is till parent of node only
                    return
            else:
                curr_path.append(node.val) 
                dfs(node.left, curr_path)
                dfs(node.right, curr_path)
                curr_path.pop()

        dfs(root,[])

        return paths
            
            