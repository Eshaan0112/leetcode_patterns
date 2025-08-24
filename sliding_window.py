''' Sliding Window Questions from Leetcode '''

# Q1
"""
Description - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=problem-list-v2&envId=oizxjoit
Level - Easy
Title - Best Time to Buy and Sell Stock
---------------------------------------
Question -
-> prices = [7,1,5,3,6,4], prices[i] = Price of given stock on day i
-> Want to max your profit by buying on day i and selling on day after ith day.
-> Return max profit possible
-> Eg: prices = [7,9,5,3,6,4], maxProfit = buy on day 2 and sell on day 5 = 6-1 = 5

Thoughts - 
-> Brute force: Calculate every possible profit by buying on every price and selling for prices after to see maxProfit at every iteration. That'd be O(n^2) time

-> Optimal:
    -> We don't need to check every possible profit in order to find the max
    -> If we're able to find elements where the buying price is higher than the selling price, we can avoid checking combinations that have the buying price.
    -> For eg: We buy at 7, but notice that 1 is smaller than the buying price, so we can completely skip checking all buy-sell options where the buying price is 7, because it is guaranteed that we have a smaller buying price to increase profit.
        -> For this we can use a sliding window where we slide the window when buy_price > sell_price
    -> Time - O(n); Space - O(1)
"""
def maxP(prices):
    # Setup
    maxProfit = 0 
    l,r = 0,1 # pointers defining the sliding window
    
    while r < len(prices): # for all elements (this is where the O(n) time comes from)
        if prices[r] < prices[l]: # selling price < buying price
            l=r # shift the window, we don't need to check these combinations
        else:
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)
        r += 1
    return maxProfit

# Q2
"""
Description - https://leetcode.com/problems/longest-substring-without-repeating-characters/
Level - Medium
Title - Longest substring without repeating characters
---------------------------------------
Question - 
-> s = "abcabcbb", soln = 3 ("abc")
-> Find length of longest substring without duplicates

Thoughts - 
-> Brute Force: Find substrings without duplicates of every character. In the worst case, time would be O(n^2)

-> Optimal: 
    -> s = "a   b   c   a   b   c   b   b"
            l---------->r                   at this step, move l+=1 (duplictate in window)
                l       r                   r+=1 (no duplicates in window)
                l           r               l+=1 (duplicate at window)
                    l       r               r += 1
                    l           r
                        l       r
                        l           r       (duplicate in window)
                            l       r       (still duplicate in window)
                                l   r       (no duplicates in window)
                                l       r   (duplicate in window)
                                    l   r   (duplicate)
                                        lr  
                                        l  r (END)
    -> We can keep track of unique elements in a window using a set
    -> Time - O(n) -> Visiting each element once; Space - O(1)   
"""

def longestLength(s):
        # Setup
        l,r = 0,0
        window_elements = set() # unique characters in each window
        longest = 0 
        
        while r < len(s):
            while s[r] in window_elements: # move left pointer till another unique element is encountered
                window_elements.remove(s[l])
                l +=1
            if s[r] not in window_elements: # add unique element to window
                window_elements.add(s[r])
                longest = max(r-l+1, longest)
            r += 1
                
        return longest
        
# Q3
"""
Description - https://leetcode.com/problems/longest-repeating-character-replacement/description/
Level - Medium
Title - Longest repeating character replacement
---------------------------------------
Question -  
-> s = "ABAB", k = 2
-> Return length of longest substring that will contain the same characters if k replacements are made at max
-> s = "ABAB", k = 2, Soln: 4 ("AAAA" or "BBBB" if we replace 2 As or 2 Bs)

Thoughts - 
-> The basic check in this problem would be how to see if replacements are allowed, because we don't have to actually replace the characters but we have to count what happens after replacement and it doesn't matter what we replace.
-> Let's say for "ABABA", k=2, we can see the character that appears most often in this string is A (3 times) and the length of the string is 5, so replacements are allowed to be 2 (length_of_string - mode_character = 5-3).
-> If the number of replacements are <=k, the string is valid, so in this case "ABABA", k=2, soln will be 5 as k=2 replacements can be done
-> If say, we had something like "AB", k=2, replacements that can be done is only 1 which is > k that means this string is not valid

-> Brute Force: Check above process for every substring. Time would be O(n^2)

-> Optimal: 
    -> s = "A   A   A   B   A   B   B" , k = 1
            l-----------r                      (r-l+1) - mode_character_count = 4 - 3 = 1 (<=k) - valid substring, length=4
            l               r                   5 - 4 = 1 (<=k) - valid substring, length=5
            l                   r               6 - 4 = 2 ( > k) - invalid substring, so shift window by l+=1
                l               r               5 - 3 = 2 ( > k) - invalid substring, so shift window by l+=1
                    l           r               4 - 2 = 2 ( > k) - invalid substring, so shift window by l+=1
                        l       r               3 - 1 = 1 (<=k) - valid substring, length=3
                        l           r           4 - 3 = 1 (<=k) - valid substring, length=4
                        l              r        END, mac length = 5
    -> Time: O(n) - Iterate on every character once; Space: O(n) - Keep track of count of character appearing max number of times in a window
"""   
def longestrepeatingreplacement(s,k):
    # Setup
    l,r = 0,0
    character_count = {} # character: count - to keep track for each window
    longest = 0 
    
    while r < len(s):
        character_count[s[r]] = 1 + character_count.get(0, s[r]) # update count of character

        while ((r-l+1) - max(character_count.values()) > k): # if substring is not valid, we shift left pointer
            character_count[s[l]] -= 1
            l += 1
            
        longest = max(r-l+1,longest)
        r += 1
        
    return longest

# Q4
"""
Description - https://neetcode.io/problems/sliding-window-maximum?list=neetcode150
Level - Hard
Title - Sliding window maximum
---------------------------------------
Question -  
-> Read the problem

-> Eg: 
Input: nums = [1,2,1,0,4,2,6], k = 3

Output: [2,2,4,4,6]

Explanation: 
Window position            Max
---------------           -----
[1  2  1] 0  4  2  6        2
 1 [2  1  0] 4  2  6        2
 1  2 [1  0  4] 2  6        4
 1  2  1 [0  4  2] 6        4
 1  2  1  0 [4  2  6]       6

Thoughts - 
    -> Brute Force:
        -> Shift through each window as given and keep track of max as you go
        -> Time: O(n*k) where n=number of elements, k=size of window --> For each window we need to find max (O(n*k))

    -> Sub-optimal:
        -> We can add each window to a max heap to get the max at that window
        -> Time: O(n log n) --> Adding to the heap is log n and has to be done n times
    
    -> Optimal:
        -> Use a monotonically decreasing double ended queue i.e DE-QUE
            -> Why a deque?
                -> O(1) to push from either end of the deque
                -> O(1) to add to the right of the deque
                -> deque = [left(front),.....,right(back)]
                -> montonically decreasing deque = [max_element, 2nd max_element, 3rd max_element,....,smallest_element]
                    -> Why monotonically decreasing:
                        -> We need to keep the max of the current window we are traversing to the left and any future max's that become the max of the next window to the right once the current max expires from the window
                            -> Eg: say our deque = [4,3,2,1] and k = 2
                                then [4,3,2,1] 
                                      --       -> current window, and max=4
                                      [4,3,2,1]
                                         ---   -> new window and now 4 is not in our new window
            -> Process of using a deque:
                -> Consider this eg: nums = [8,7,6,9], k=2
                    -> Process 
                    Step1: 8  7  6  9
                           ----             -> deque = [8,7] since 7<8, our deque would be monotonically decreasing if we add 7 (7 can potentially the max of the next window)
                                            -> res = [8] -> left most value in the deque will be the max of the current window, so we can add that to our result
                    
                    
                    Step2: 8  7  6  9
                              ----          -> 8 is no longer in our window, so we pop from the left (O(1)); deque = [7]
                                            -> deque = [7,6] since 6<7, our deque would be monotonically decreasing if we add 6
                                            -> res = [8,7] -> left most value in the deque will be the max of the current window, so we can add that to our result 
   
                    Step3: 8  7  6  9
                                 ----       -> 7 is no longer in our window, so we pop from the left (O(1)); deque = [6]
                                            -> Now we have 9 and we check if 9 > 6, that means we need to pop the right most position (NOT THE LEFT!)
                                            -> We keep popping from the right till we get an element > 9. It just so happens that our deque=[6], so we end up popping just 6 and get deque = [9]
                                            -> res = [8,7,9]: FINAL RESULT
"""
def maxSlidingWindow(nums, k):
        '''
        NOTE: We are storing indices in the de-que for this problem
        '''
        res = [] # max of each window - final output
        l,r = 0,0 # pointers to slide window
        
        de_que = deque() # [left(front),...........,right(back)]

        while r<len(nums): # as long as we don't reach end of input

            # Remove values that are smaller in the current window as they can never be the max in the current window or any future windows
            while de_que and nums[de_que[-1]] < nums[r]: # nums[de_que[-1]] is the rightmost value of the deque
                de_que.pop() # FROM RIGHT --> O(1)
            
            # Add element to the queue --> the max of the current window
            de_que.append(r) 

            # Remove the element that expires once the window is shifted
            if l > de_que[0]:
                de_que.popleft() # FROM LEFT --> O(1)
            
            '''Edge case: we only need to update left pointer if our window is of the given size
            At the very start, the window is still growing - it isn’t size k yet.
            We only want to record results (and slide the left pointer l) once the window reaches size k'''
            if (r-l+1) == k:
                res.append(nums[de_que[0]]) # Add the leftmost value to the result as it contains the max of the current window
                l += 1
            r += 1 # keep growing the window
        
        return res
        
            
    
    