class Solution:
    def combinationSum(self, n, k):
        ans = []

        def backtrack(start, path, total):
            
            # Valid combination
            if len(path) == k:
                if total == n:
                    ans.append(path[:])
                return

            # Try numbers from start to 9
            for num in range(start, 10):
                
                # Pruning
                if total + num > n:
                    break

                path.append(num)

                backtrack(num + 1, path, total + num)

                path.pop()

        backtrack(1, [], 0)

        return ans