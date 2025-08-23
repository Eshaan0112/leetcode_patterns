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

