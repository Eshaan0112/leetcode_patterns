''' Min/Max heaps
NOTE: Python only has min heaps, so need to multiply by -1 to get max heap elements
-> Heaps:
Heaps (min heaps) are just a binary tree arranged something like:

                            smallest element
            2nd smallest                        3rd smallest
4th smallest        5th smallest        6th smallest        7th smallest

-> Code:
    -> heapq.heapify(array) -> O(n) to convert array to heap
    -> heapq.heappop(array) -> Pop the nth minimum element in O(log n) time
    -> heapq.heappush(array) -> Adds the nth minimum element in the right position in O(log n) time

'''