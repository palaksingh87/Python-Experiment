class Solution:
    def minSwap(self, arr, k):
        n = len(arr)
        
        # Step 1: count good elements (<= k)
        good = 0
        for x in arr:
            if x <= k:
                good += 1
        
        # Edge case: no need to swap
        if good == 0 or good == n:
            return 0
        
        # Step 2: count bad elements in first window
        bad = 0
        for i in range(good):
            if arr[i] > k:
                bad += 1
        
        min_swaps = bad
        
        # Step 3: slide window
        for i in range(good, n):
            # remove left element
            if arr[i - good] > k:
                bad -= 1
            
            # add right element
            if arr[i] > k:
                bad += 1
            
            min_swaps = min(min_swaps, bad)
        
        return min_swaps