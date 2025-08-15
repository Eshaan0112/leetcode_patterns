''' Quicksort algorithm to find kth largest/smallest element

FOR FINDING Kth SMALLEST ELEMENT
Intuition: Imagine partioning an array with a pivot(any element in the array i.e random start) such that elements to the left of the pivot are < than pivot and elements to the right of the pivot are > the pivot

->If k < pivot index, then we recur for the left part
->If index is the same as k, we have found the k-th smallest element and we return
->If k > pivot index , then we recur for the right part
This reduces the expected complexity from O(n log n) to O(n), with a worst-case of O(n^2)

NOTE: Simply reverse the above conditions for finding kth largest element

-> Time Complexity:
    -> If the pivot always splits the array perfectly in half:

        1st partition: n elements

        2nd partition: n/2 elements

        3rd partition: n/4 elements
        ...and so on.

        Work done = n + (n/2) + (n/4)... = 2n ~ O(n)
    
    -> If the pivot is random, the expected split is reasonably balanced (not perfect, but not awful).
        On average, you only keep half the array each step, so you still get O(n)
    
    -> If the pivot is always the smallest or largest element:

        1st partition: n elements (throw away only 1 element)

        2nd partition: n-1 elements

        3rd partition: n-2 elements
        ...and so on.

        Work done = n + (n-1) + (n-2).. ~ O(n^2)
    -> CODE:
     def quickselect(l,r):
            """ Recursive function that runs quickselect algo on a partition between (l,r) """
            pivot = nums[r] # random choice of pivot
            p = l # pointer that moves through the partition to separate the elements

            for i in range(l,r):
                if nums[i] <= pivot:
                    # Swap and put elements smaller than pivot to the left portion of the array
                    nums[p], nums[i] = n hums[i], nums[p]
                    p+=1 # increment this because next time we want to swap at p, it should be at the next position
            # Swap the pivot value (which was at the absolute right) to the position of the partition (half of the array, ideally)
            nums[p], nums[r] = pivot, nums[p]

            # Have we found the solution? If not, then we need to select which partition to search in
            if p==k: return nums[p] 
            elif p < k: return quickselect(l,p-1)
            else: return quickselect(p+1,r)
'''
