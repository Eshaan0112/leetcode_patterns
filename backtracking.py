''' Backtracking questions from Neetcode

VANILLA BACKTRACKING:
-> Think in terms of branching a tree (it's possible it can have > 2 branches) or just a binary (to include or not to include) choice.
-> Questions where we need to list all possible solutions of a given problem is the main use case for this approach
-> It's a brute force approach and in terms of code, follows a template like:
     
    def f():
    
        # operations 

        # Recursively backtrack
        def backtrack(i):
            # Base case 
            if some_condition:
                # reached leaf in our backtracking tree as all subsets will be in leaves
                # remember if you're dealing with an array of sorts, you might want to do a copy of it here since its reference may be modified in future steps
                return something

            # Choose to do something (maybe .append to an array)
            backtrack(i+1) # explore all paths where we chose to do something. If repeated selection is allowed, you don't need to do i+1, you can simply call backtrack(i)

            # choose not to do something (maybe .pop after exploring what happens after appending)
            backtrack(i+1) # explore all paths where we chose not to do something
        backtrack(0) # start from 0th index
        return something
-> Time Complexity: O(2^n) --> 2 choices for n elements

AVOIDING DUPLICATES:
-> Think sorting
-> In terms of application, say we are to avoid duplicates in a binary choice approach. Then we notice that the duplicates occur in between
paths that are chosen to be included and not to be included. For eg, let's say input = [1,2,1] and we're making subsets
                                    *
                        1                     []
                    12      1               2       []
                121  12   11  1           21
    In the leaves, choice to include 1 at the first level leads to [12] in the leaf and then choice not to include 1 leads to [21]. [12] and [21] are duplicates.
    We need to make it so that once we've traversed the choice-to-include "subtree" using duplicate elements i.e both 1s in input, we make sure we skip the duplicates before we start our traversal
    down the path of choice-not-to-include or the right "subtree". In the code, this should be done after popping back up as shown below:
    
def f():
        # operations 

        # Recursively backtrack
        def backtrack(i):
            # Base case 
            if some_condition:
                # reached leaf in our backtracking tree as all subsets will be in leaves
                # remember if you're dealing with an array of sorts, you might want to do a copy of it here since its reference may be modified in future steps
                return something

            # Choose to do something (maybe .append to an array)
            backtrack(i+1) # explore all paths where we chose to do something

            # choose not to do something (maybe .pop after exploring what happens after appending)
            
            ## avoid duplicates right after popping
            while i+1<len(input) and input[i] == input[i+1]:
                i += 1
            
            backtrack(i+1) # explore all paths where we chose not to do something
        backtrack(0) # start from 0th index
        return something                    
'''


''' Vertical Path Solutions (i.e in a tree, each path is a solution)
->Code:
    def main(input):
        # intialize things to be returned
        def dfs(i):
            # Base cases
                
            # Explore each vertical path
            for j in range(i, len(input)):
                parts.append(input[i:j+1])
                dfs(i=j+1)
                parts.pop()
        dfs(0)
        return whatever
        
    -> How the vertical paths are being built (Consider Q2 below, Palindrom Partitioning - the visual explanation is shown only till "ab"):
                                                    "a"                 "aa"             "aab"     
                                                "a"     "ab" (here!!)
                                                "b"
                
            
            -> dfs(i=0) => j = 0                                 ,                                j=1               ,..                                    j=2  
                               |
                               |
                check s[i:j+1],s[0:1]->"a"(Palindrome)
                               |
                               |
                               dfs(i=1) => j = 1 ,..                                           j=2 (here i=1, j=2, so we check s[i:j+1] which is "ab") 
                                               |                                                  |
                                               |                                                  |
                                    check s[i:j+1],s[1:2]->"a"(Palindrome)                        |
                                               |                                                  |
                                               |                                       pop(a), j is moved forward as part of the for loop
                                               dfs(i=2) => j = 2                           nothing to explore as j == len(s)  
                                               |                                                  |
                                               |                                       pop(b), j is moved forward as part of the for loop
                                    check s[i:j+1], s[2:3]->"b"(Palindrome)                       |
                                               |                                                  |
                                               |                                                  |
                                               dfs(i=3) => out of bounds -> res = [["a","a","b"]] |
                                               
                                          
                               

'''         
# Q1
"""
Description - https://neetcode.io/problems/permutations?list=neetcode250
Title - Permutations
Level - Medium
---------------------------------------
Question - 
-> Given unique ints, list all possible permutations
-> Eg:
    input = [1,2,3]
    soln = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Thoughts - 
-> "all possible" --> brute force --> backtracking

-> Difficult brute force:
                                                                                     *
all 3 available for us to choose                                    1                2              3
2 out of 3 available for us to choose                           2       3        1       3      1       2
1 out of 3 available for us to choose                           3       2        3       1      2       1    
    -> See the vertical paths (all paths)- they are the permutations.
    -> This way is possible and gives an intuition about why permutations are n!

-> Easy brute force:
    -> Let's not think in terms of branching
    -> Say we have [1,2,3] 
        -> Building permuatations of [1,2,3] involves moving "1" through all positions of all permutations of [2,3]
                -> Moving 1 through all positions of [2,3] and [3,2] gives us [1,2,3],[2,1,3],[2,3,1] and [1,3,2],[3,1,2],[3,2,1] respectively
            -> Building permutations of [2,3] involves moving "2" through all permuations of [3]
                -> Moving 2 through all positions of [3] gives us [2,3] and [3,2]
        -> This gives a recursive subproblem in that the subproblem is getting permutations (by moving through possible positionsm) of the sublist by excluding the element which we want to keep locked
        -> [1,2,3]   ---> return with [1,2,3],[2,1,3],[2,3,1] and [1,3,2],[3,1,2],[3,2,1]
            [2,3]  ----> pop back up with [2,3] and [3,2] 
            [3] ----> pop back up with [3] since [3] is the only permuation of [3]
        -> We just need to realize all permutations: [a or b or c, a or b or c, a or b or c] can be built by having permuations of [b,c] and so on
            -> Building the permutations needs the realization that we need to place the "excluded" element (a) at every possible position of every permutation of [b,c]
            
        -> Time: O(n!)
        """ 

def permute(self, nums):
        res = [] # contains all permutations, n! of them where n=len(nums)

        # Recursive call to get permutations of sublist of nums i.e nums minus the first element
        '''
        If we're recursing for nums = [1,2,3], the recursive stack would be something like
        permute([1,2,3]) --> permute([2,3]) --> permute([3]) --> permute([])
           nums[0] = 1        nums[0] = 2        nums[0] = 3        
                            return [[2,3],[3,2]] return [[3]]    return[[]]
        '''

        # Base case
        if len(nums) == 0: return [[]] 
        permutations = self.permute(nums[1:]) # nums[0] is excluded 

        for p in permutations: # for all perutations for a sublist of nums
            for i in range(len(p)+1): # for all possible positions where nums[0] can be inserted
                '''
                say we are at p=[2,3] for permutations= [[2,3],[3,2]], i here tells us what positions nums[0]=1 can
                be positioned at. If we position 1 at every possible i, then we get all permutations for this p
                like: i=0 ([1,2,3]); i=1 ([2,1,3]); i=2 ([2,3,1])
                '''
                snapshot_of_permutation = p.copy()
                snapshot_of_permutation.insert(i, nums[0]) 
                res.append(snapshot_of_permutation)
        
        return res

# Q2
"""
Description - https://neetcode.io/problems/palindrome-partitioning?list=neetcode250
Title - Palindrome Partitioning
Level - Medium
---------------------------------------
Question -
    -> Given a string s, split s into substrings where every substring is a palindrome
    -> Eg: s = "aab"
           Soln: [["a","a","b"],["aa","b"]]
Thoughts - 
    -> We will essentially need to check all possible partitions
    -> Possible choices of partitions can be derived by cutting the input array at each position, so first choice would be:
        "a"               "aa"              "aab"
        -> For leftmost "a", we've cut as "a" | "ab"     
        -> We can further split the right part "ab" by performing two cuts- "a" | "b" AND "ab"|, so the branch starting with "a" will look like:
                        "a"                 "aa"             "aab"     
                    "a"     "ab"
                    "b"
    
        -> Look at the vertical paths - these are the possible partitions and we need to check each of these paths to see if they're palindromes
                 
                                     
"""

def partition(self,s):
        
        res = [] # store all palindromic partitions
        parts = [] # partitioned substrings 

        def dfs(i):
            """ DFS backtrack starting at ith level of recursive tree """
            
            # Reached end of string, s
            if i == len(s):
                res.append(parts.copy())
                return
            
            # Explore each vertical path
            for j in range(i, len(s)):
                if self.isPali(s,i,j): # check if substring s[i:j+1] is a palindrome
                    parts.append(s[i:j+1])
                    dfs(i=j+1)
                    parts.pop()
        dfs(0) # trigger
        return res
        
def isPali(self, s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True