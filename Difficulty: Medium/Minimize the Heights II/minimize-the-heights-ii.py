class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        
        # Sort the array
        arr.sort()
        
        # Initial difference
        ans = arr[n - 1] - arr[0]
        
        # Traverse the array
        for i in range(1, n):
            
            # Skip if height becomes negative
            if arr[i] - k < 0:
                continue
            
            # Minimum height after modification
            minimum = min(arr[0] + k, arr[i] - k)
            
            # Maximum height after modification
            maximum = max(arr[i - 1] + k, arr[n - 1] - k)
            
            # Update answer
            ans = min(ans, maximum - minimum)
        
        return ans