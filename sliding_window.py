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


        
            
    
    