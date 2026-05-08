from bisect import bisect_right

class Solution:
    def median(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        low = 1
        high = 2000  # constraint max value
        
        desired = (n * m) // 2
        
        while low <= high:
            mid = (low + high) // 2
            
            # count elements <= mid
            count = 0
            for row in mat:
                count += bisect_right(row, mid)
            
            if count <= desired:
                low = mid + 1
            else:
                high = mid - 1
        
        return low