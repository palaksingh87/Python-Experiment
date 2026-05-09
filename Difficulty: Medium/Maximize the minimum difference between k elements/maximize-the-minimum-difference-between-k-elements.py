class Solution:
    def maxMinDiff(self, arr, k):
        arr.sort()

        # Check if minimum difference 'dist' is possible
        def canPlace(dist):
            count = 1
            last = arr[0]

            for i in range(1, len(arr)):
                if arr[i] - last >= dist:
                    count += 1
                    last = arr[i]

                    if count >= k:
                        return True

            return False

        left = 0
        right = arr[-1] - arr[0]

        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if canPlace(mid):
                ans = mid
                left = mid + 1   # try bigger difference
            else:
                right = mid - 1  # try smaller

        return ans