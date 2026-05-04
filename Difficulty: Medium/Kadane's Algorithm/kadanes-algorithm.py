class Solution:
    def maxSubarraySum(self, arr):
        max_sum = float('-inf')
        current_sum = 0

        for x in arr:
            current_sum += x
            max_sum = max(max_sum, current_sum)

            if current_sum < 0:
                current_sum = 0

        return max_sum