''' BFS Traversal questions from Neetcode - generally used to solve minimizing problems'''
# Q1
"""
Description - https://neetcode.io/problems/open-the-lock?list=neetcode250
Title - Open the Lock
Level - Medium
---------------------------------------
Question - 
-> Too big - read the description
-> Eg: 
Input: deadends = ["1111","0120","2020","3333"], target = "5555"
Soln: 20 (5 moves for 1st digit, 5 moves for second, 5 moves for third, 5 moves for fourth)

Thoughts - 
-> Visualize an input:
At the start we are given that we'll be starting with "0000"

                                                            0000
possible options(move 1):    1000;9000               0100;0900           0010;0090;          0001;0009   
possible options(move 2)    1100,1900;9100;9900.........(it is possible to recreate a combination here, so we'll also keep a visit set)
-> If we choose a DFS approach, it'll be too computationally expensive to find the minimum number of moves to reach a given target
-> BFS goes level by level so move 1 is level 1 and move 2 is level 2 i.e the minimum moves needed to reach any of the combinations in level 1 is 1
-> At each digit, there are two possibilities - increment by 1 and decrement by 1
    -> Increment by 1: (digit+1) % 10 = digit
    -> Decrement by 1: (digit-1 + 10) % 10 = digit (Eg: if we have "0" and we are to decrement by 1 i.e 0-1 => (0-1 + 10) % 10 = 9 which is what we want if we decrement 0 by 1 (as the wheels are cyclic)
-> We do a simple BFS where we generate the combinations at each level. If we find the target combination, we return it
-> Time Complexity: O(10^4)-> Each digit can take 10 possible values and there are 4 digits in each combo
"""

class Solution:
    def openLock(self,deadends, target):

        
        # Setup
        combo, moves = "0000",0
        if combo in deadends: return -1 # edge case
        queue = deque([(combo, moves)]) # store the number of moves it takes to reach combo at each level
        visit = set(deadends) # clever way to add deadends to the visit set, so we can exit if we encounter any of the combos given in "deadends"

        # BFS
        while queue:
            combo, moves = queue.popleft()
            if combo == target:
                return moves # target found; moves is always going to be the least possible value since we're doing BFS
            
            # Generate the combinations from the current combo for the next level and add them to the queue
            children = self.generate_combos(combo) # helper 
            for child in children:
                if child not in visit: # check deadend or if we've already visited a combo
                    visit.add(child)
                    queue.append((child,moves+1)) # level = moves + 1
        return -1 
    
    def generate_combos(self, combo):
        """ Helper to generate unique combinations by incrementing and decrementing wheel digits for a given combination lock for one level (move)"""
        
        all_level_combinations = [] # all these combinations can be reached in the same move
        for i in range(4): # there are 4 wheels (digits)
            # For each wheel, we want to add +1 position and -1 position

            # +1 position
            digit = str((int(combo[i]) + 1) % 10) # increment digit at position i
            all_level_combinations.append(combo[:i] + digit + combo[i+1:]) 
            
            # -1 position
            digit = str((int(combo[i]) - 1 + 10) % 10) # decrement digit at position i
            all_level_combinations.append(combo[:i] + digit + combo[i+1:]) # replace digit at position i
        
        return all_level_combinations
            
        