from bisect import bisect_left

class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        
        max_ones = 0
        result_row = -1
        
        for i in range(n):
            # first index of 1 in row i
            idx = bisect_left(arr[i], 1)
            
            ones = m - idx
            
            if ones > max_ones:
                max_ones = ones
                result_row = i
        
        # if no 1 found anywhere
        return result_row if max_ones > 0 else -1