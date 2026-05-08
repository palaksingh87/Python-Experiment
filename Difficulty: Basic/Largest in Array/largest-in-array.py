class Solution:
    def largest(self, arr):
        # Initialize the largest element as the first element
        largest = arr[0]
        
        # Traverse the array
        for num in arr:
            if num > largest:
                largest = num
                
        return largest
        
