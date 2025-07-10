''' Ancestor Problems from Leetcode '''

# Q1
"""
Description - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
Title - Lowest Common Ancestor of a BST
---------------------------------------
Question - 
-> Given a BST and two nodes find lowest common ancestor of the two
-> Eg:
    bst: 
                            6
                    2               8
                0       4       7       9   
                      
    p = 2, q=8, Soln: Lowest common ancestor = 6
    p = 2, q = 4 Soln: Lowest common ancestor = 2
    
Thoughts - 
-> We need to find where the left and right split is
-> In a BST, all elements to the left < root and all elements to the right > root
-> If our given nodes are smaller than root, we know we'll find the split to the left and vice-versa
-> We'll need to recursively search subtrees to the left or right to find the split
"""

def LCA(root,p,q):
    '''
    if p and q < root: left_subtree
    if p and q > root: right_subtree
    if split found: return root
    '''

    # Time: O(height_of_tree) --> recurisve call stack would go as we search subtrees
    # Space: O(height_of_tree)

    # Edge case
    if not p or not q or not root: return None

    # Recursion
    if p.val < root.val and q.val < root.val:
        # Left subtree search
        root = root.left
        return LCA(root, p,q)

    elif p.val > root.val and q.val > root.val:
        # Right subtree search
        root = root.right
        return LCA(root, p,q)
    else:
        # Split found
        return root

# Q2
"""
Description - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
Title - Lowest Common Ancestor of a Binary Tree
---------------------------------------
Question - 
-> Find lowest common ancestor of two nodes in a binary tree

Thoughts - 
-> We will need to look at each node present in the tree, since we don't have any property that can help us in our navigation
-> Say our tree is 
                                    3
                                4       5
                            6       7
                                  2   8
                                  and p=6,q=8
                                  
-> We search left and right from the root and at every node we check if we've found p or q -> sort of like Post Order Traversal
-> Once we reach node 6, we return its value to the location of 4 (recrusive calls propogation) and search right of node 4
-> Once we reach node 8, we return its value to location of 7. 
-> At this point, the left of 4 has node 6 and right of node 4 has node 8..Since both are non-null, we return their location's root that is node 4 which is the final answer
-> Time: O(n) -> Check every node; Space: O(height_of_tree) -> recursive call stack
"""

def LCA(root, p,q):
    # Compare every node we visit to p,q
    if not root: return None # if at leaves or tree is NULL -> BASE CASE
    if root == p or root == q:# we found atleast one of the nodes, so it's possible that it itself is the root
        return root
    
    # POST ORDER TRAVERSAL (l,r,root)
    # If we didn't find p or q in our current node, we search left and right of our current node
    left = LCA(root.left,p,q)  
    right = LCA(root.right,p,q) 
    if left and right: # if on our search, we find p and q in left and right subtree respectively, we've found our split or LCA
        return root

    # Propogate the "found" value (p or q) up the tree
    return left if left else right 