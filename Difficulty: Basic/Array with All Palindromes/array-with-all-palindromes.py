class Solution:
    def isPalindrome(self, x):
        original = x
        rev = 0
        
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        
        return rev == original

    def isPalinArray(self, arr):
        for num in arr:
            if not self.isPalindrome(num):
                return False
        return True