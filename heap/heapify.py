''' Min/Max heap questions from Neetcode 
NOTE: Python only has min heaps, so need to multiply by -1 to get max heap elements
-> Heaps:
Heaps (min heaps) are just a binary tree arranged something like:

                            smallest element
            2nd smallest                        3rd smallest
4th smallest        5th smallest        6th smallest        7th smallest

-> Code:
    -> heapq.heapify(array) -> O(n) to convert array to heap
    -> heapq.heappop(array) -> Pop the nth minimum element in O(log n) time
    -> heapq.heappush(array, element) -> Adds the nth minimum element in the right position in O(log n) time
'''

# Q1
"""
Description - https://neetcode.io/problems/task-scheduling?list=neetcode150
Title - Task Scheduler
Level - Medium
---------------------------------------
Question - 
-> Read problem
-> Eg:
    tasks = ["X","X","Y","Y"], n = 2
    Soln: 5 --> X->Y--idle--X->Y

Thoughts - 
-> We can think about this where we need to process the more frequently occuring task first to minimize the time. 
    -> Say we have "AAABBCC"
        {A:3, B:2, C:2}
        -> We start with A then B then C with our tasks processed looking like "ABC" and our new map {A:2,B:1,C:1}
        -> Then we see A is still the most frequent so we do "ABC" again for a final task process list of "ABCABC" and a map like: {A:1,B:0,C:0}
        -> We're just left with A to process so we process that for a total min time fo 7 without having to wait for any of the tasks
        -> To continuously figure out which task is the most frequent we can use a max heap
-> We will also be using a queue in this problem to determine which task is possible to be processed like this:
    -> Eg: "AAABBCC", n = 1, SOLN: 7
        -> maxHeap will store count of each task at each time stamp
        -> queue will store 2 things: (decremented count of processed task, time at which we can process this task again i.e at which time stamp can we add this task back to our max heap to process)
        -> time = 0 
        -> Step1: 
                maxHeap = [3,2,2] # process A and add its next process possibility to queue
                We process (pop) 3 (since its most frequent) at time = 1
                maxheap = [2,2] queue = ([3-1 (decremented task count of A), time+n (Time stamp at which the decremented count of A can be processed)]) = ([2,2]) --> Task with count 2 can be processed when the time stamp reaches 2 
        -> Step2:
                maxheap = [2,2] # B,C 
                We process 2 at time = 2 # process B and add to queue
                maxheap = [2] --> C remaining, queue = ([2,2],[2-1,2+n]) = ([2,2],[1,3])
                **notice that the first element in the queue can be popped now since the time stamp=2 has reached
                maxheap = [2,2] --> A added, queue = ([1,3]) # popped from queue and added back to maxheap to process
        -> Step3:
                maxheap = [2,2] # A,C
                We process 2 at time = 3 # process A again
                maxheap = [2] --> C remaining, queue = ([1,3],[1,4]) # [1,3] is for B;, [1,4] is for A
                **notice that the first element in the queue can be popped now since the time stamp=3
                maxheap = [1,2] --> B added and C remaining, queue = ([1,4])
        -> Step4:
                maxheap = [1,2] # B,C
                We process 2 (most frequent) at time = 4 # process C
                maxheap = [1] --> B remaining, queue = ([1,4],[1,5]) # [1,4] is for A; [1,5] is for C
                **notice that the first element in the queue can be popped now since the time stamp=4
                maxheap = [1,1] --> A added, B remaining, queue = ([1,5])
        -> Step5: 
                maxheap = [1,1]
                --> We dont need to add anything to the queue since the process count reaches 0
                We process 1 at time =5
                maxheap = [1] --> A complete, B remaining
                **notice that the first element in the queue can be popped now since the time stamp=5
                maxheap = [1,1] --> C added, B remaining, queue = ()
        -> Step6:
                maxheap = [1,1]
                --> We dont need to add anything to the queue since the process count reaches 0
                We process 1 at time = 6
                maxheap = [1] --> C complete, B remaining
        -> Step7:
                maxheap = [1]
                --> We dont need to add anything to the queue since the process count reaches 0
                We process 1 at time = 7
                maxheap = () --> A,B,C complete
                queue = ()
        RETURN            
"""

def leastInterval(tasks,n):

        # Get the maxheap and queue to start processing tasks
        count = Counter(tasks) # {A:3, B:2, C:2} --> just to get the count, we don't care about the characters
        maxheap = [-num for num in count.values()] # python only has min heaps!
        heapq.heapify(maxheap) 
        time_stamp = 0 # keep track of time at each processing step
        q = deque() # pairs of [decremented task count, next timestamp for process] --> since this is a modified min heap, we will have to increment the count to simulate decrementing it because our numbers are negative

        # Start processing
        while maxheap or q: # tasks left to process
            time_stamp += 1
            
            # Process the most frequent task
            if maxheap:
                count = heapq.heappop(maxheap)
                count += 1 # decrement the count of the task being processed by 1. Again remember we are simulating a max heap which is why we have to add 1 to decrement
                
                if count!=0: # more count of this task is remaining, so add to queue
                    q.append([count, time_stamp + n]) # n is the idle time
            
            # At this time_stamp, if there is some count of the "first in" task that can be processed, add it to maxheap
            if q and q[0][1] == time_stamp:
                val = q.popleft()[0]
                heapq.heappush(maxheap, val) # val needs to be processed 
        
        return time_stamp


