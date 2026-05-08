class Solution:
    def factorial(self, n):
        fact = 1

        # Calculate factorial
        for i in range(2, n + 1):
            fact *= i

        # Convert factorial to list of digits
        return [int(digit) for digit in str(fact)]