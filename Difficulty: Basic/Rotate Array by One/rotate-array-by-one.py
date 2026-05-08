class Solution:
    def rotate(self, arr):
        # Store the last element
        last = arr[-1]
        
        # Shift elements one position to the right
        for i in range(len(arr) - 1, 0, -1):
            arr[i] = arr[i - 1]
        
        # Place last element at the first position
        arr[0] = last
        
        return arr