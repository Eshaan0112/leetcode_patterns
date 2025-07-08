''' Math and Geometry questions from Leetcode - resemble Q3 for Codesignal OA

In questions like these, we don't need to worry too much abut time complexity. Just do what you're told.
'''

# Q1
"""
Description - https://leetcode.com/problems/spiral-matrix/description/
Level - Medium
Title - Spiral Matrix
---------------------------------------
Question - 
-> Traverse a 2D matrix in spiral order
-> 
1   2   3           
4   5   6 --------> 1   2   3   6   9   8   7   4   5
7   8   9

Thoughts -
    ->  LOOP till t<b, l<r :
                l         r
            t   1   2   3       -> l--->r (topleft->topright) traversal: 1->2->3 - update t+=1
                4   5   6         
                7   8   9
            b
            
                l       r
                1   2   3       -> t--->b (topright->bottomright) traversal: 6->9 - update r-=1
            t   4   5   6         
                7   8   9
            b
            
            -------------> At this point where we've moved topleft->topright and topright to bottomleft, it is possible we've completed our traversal. Consider 1->2->3 matrix and dry run it. If we continue to move bottomright to bottom left, we'll print out 1 2 3 2 1 and not 1 2 3. Hence, we must check if l<=r or t<=b at this step and exit if that's the case.
                l       r
                1   2   3       -> r--->l (bottomright->bottomleft) traversal: 8->7 - update b-=1
            t   4   5   6         
                7   8   9
            b
            
                l       r
                1   2   3       -> b--->t (bottomleft->topleft) traversal: 7->4 - update l+=1
            t   4   5   6         
            b   7   8   9
            
            go to next iteration of LOOP :  next iteration of loop will have            l   r
                                                                                    1   2   3       
                                                                                t   4   5   6         
                                                                                b   7   8   9
            
    
    -> Time: O(n*m), where n*m is size of matrix ; Space: O(n*m)   
"""
def spiral_matrix(matrix):
        # Setup
        l,r = 0, len(matrix[0]) # to traverse rows
        t,b = 0, len(matrix) # to traverse columns
        spiral_order = []

        # Traversal
        while l<r and t<b:
            # Top left to top right first
            for i in range(l,r):
                spiral_order.append(matrix[t][i])
            t += 1 # move top down for next iteration

            # Top right to bottom right second
            for i in range(t,b):
                spiral_order.append(matrix[i][r-1])
            r -= 1 # move right one position to left for next iteration
            
            # It is possible we reach invalidity here
            if not (l < r and t < b):
                break

            # Bottom right to bottom left
            for i in range(r-1,l-1,-1): # reverse order
                spiral_order.append(matrix[b-1][i])
            b -= 1 # move bottom up for next iteration

            # Bottom left to top left
            for i in range(b-1,t-1,-1): # reverse order
                spiral_order.append(matrix[i][l])
            l += 1 # move left one position to the left for next iteration

        return spiral_order

# Q2
"""
Description -https://leetcode.com/problems/diagonal-traverse/
Level - Medium
Title - Diagonal traversal
---------------------------------------
Question - 
-> m*n matrix to be traversed in diagonal order
-> 
    1 2 3                                     
    4 5 6   -------> 1,2,4,7,5,3,6,8,9  
    7 8 9 

Thoughts - 
-> There are two diagonal directions - one going up and another going down
-> If going up (eg diagonal 7->5->3) then next element to be added are (i+1,j-1)
-> If going down (eg diagonal 2->4) then next element to be added are (i-1,j+1)
-> Once each diagonal is traversed, there is the next diagonal to traverse in the opposite direction, so if we've done 7->5->3 in upward direction, we need to traverse 6->8 in downward direction
-> When traversing a diagonal after the previous diagonal traversal, we need to find the head or the starting element of the new diagonal. If we traversed upward diagonal, we need to find head of next downward diagonal and vice-versa
-> Time: O(n*m), where n*m is size of matrix ; Space: O(n*m)
"""
class Solution:
    def findDiagonalOrder(self, mat):

        # Setup
        up = True # up direction first
        R, C = len(mat), len(mat[0])
        i,j = 0,0 # pointers to select elements of diagonal
        res = []

        # Traversal
        while i<R and j<C:
            res.append(mat[i][j]) # add current element

            # Update potential pointer position
            if up: 
                # next element of upward diagonal will be [i-1,j+1]
                next_i = i - 1
                next_j = j + 1
            else:
                # next element of downward diagonal will be [i+1,j-1]
                next_i = i + 1
                next_j = j - 1

            # Check if the next element in the diagonal is within the
            # bounds of the matrix or not. If it's not within the bounds,
            # we have to find the next head. 

            if (next_i < 0 or next_i==R) or (next_j < 0 or next_j==C): # out of matrix bounds
                # Find head
                if up: # if currently traversed an upward diagonal
                    # find head of diagonal going down next
                    i,j = self.find_head(i,j,R,C,up)
                    up = False
                else: # if currently traversed a downward diagonal
                    # find head of diagonal going up next
                    i,j = self.find_head(i,j,R,C,up)
                    up = True
            else: # within matrix bounds
                i = next_i
                j = next_j
        
        return res
    
    def find_head(self, i,j,R,C,up):
        """ Find head of next diagonal based on traversal direction """
        
        if up:
            # For an upwards going diagonal having [i, j] as its tail
            # If [i, j + 1] is within bounds, then it becomes
            # the next head. Otherwise, the element directly below
            # i.e. the element [i + 1, j] becomes the next head
            if (i<R and j+1<C):
                return i,j+1
            else:
                return i+1,j
        else:
            # For a downwards going diagonal having [i, j] as its tail
            # if [i + 1, j] is within bounds, then it becomes
            # the next head. Otherwise, the element directly below
            # i.e. the element [i, j + 1] becomes the next head
            if (i+1<R and j<C):
                return i+1, j
            else:
                return i,j+1
            

# Q3
"""
Description - https://leetcode.com/problems/reshape-the-matrix/
Level - Easy
Title - Reshape Matrix
---------------------------------------
Question - 
-> Reshape a mxn matrix into rxc
-> 
1 2 
3 4   r = 1,c = 4 ---> Soln: 1 2 3 4

Thoughts - 
-> Flatten the array so that it is a single list of shape 1 x (m*n)
-> Compare the size with the new dimensions r*c. If the size matches, the reshaping is possible.
-> To reshape, we need to slice the flattened array by selecting elements that'll go row-wise (refer to dry run eg in code below)
-> Time: O(n*m + r*c); Space: O(r*c + m*n)
"""     
def reshape(mat,r,c):
    flat_mat = [] # flattened matrix with dimensions 1 x (m*n)
    res = [] # resultant matrix with new dimensions r x c

    M, N = len(mat), len(mat[0]) # original dimensions, m x n

    for row in range(M):
        flat_mat.extend(mat[row]) # [[1,2][3,4]] ---> [1,2,3,4]
    
    # Check validity of r x c dimensions
    if not (r*c == len(flat_mat)):
        # Invalid dimensions
        return mat 
    else:# Reshape
        # [[0,  1,  2,  3],
        #  [4,  5,  6,  7],    m x n = 3 x 4             ->       r x c = 2 x 6         [[0,  1,  2,  3,  4, 5],
        # [8,  9,  10, 11]]                                                               [6,  7,  8,  9,  10, 11]]

        # flat_mat =                                [0,   1,  2,  3,  4,  5,  6,  7,  8,  9,  10  ,11]
        # first_row_needed = start=i*c=0*6=0       start                     end
        #                    end=i*c+c=0*6+6=6

        # second_row_needed = start=i*c=1*6=6
        #                     end=i*c+c=1*6+6=12                            start                       end
        for i in range(r):
            start = i*c
            end = i*c + c
            res.append(flat_mat[start: end])
    return res
    
