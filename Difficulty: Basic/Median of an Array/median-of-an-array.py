class Solution:
    def findMedian(self, arr):
        arr=sorted(arr)
        median=len(arr)//2
        return arr[median] if len(arr)%2!=0 else (arr[median-1]+arr[median])/2