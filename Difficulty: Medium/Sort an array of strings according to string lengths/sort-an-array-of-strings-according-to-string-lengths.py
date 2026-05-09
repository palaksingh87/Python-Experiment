class Solution:
    def sortByLength(self, arr):
        
        # Stable sort by string length
        arr.sort(key=len)
        
        return arr