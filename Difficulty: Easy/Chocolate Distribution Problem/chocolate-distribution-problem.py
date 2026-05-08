class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        
        if m == 0 or n == 0 or m > n:
            return 0
        
        # Step 1: Sort the array
        arr.sort()
        
        min_diff = float('inf')
        
        # Step 2: Sliding window of size m
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            min_diff = min(min_diff, diff)
        
        return min_diff