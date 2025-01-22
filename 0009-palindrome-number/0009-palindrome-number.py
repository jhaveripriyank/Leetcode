class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        reversed = original[::-1]
        return original == reversed        