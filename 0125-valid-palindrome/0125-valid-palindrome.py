class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(char.lower() for char in s if char.isalnum())
        return new_s == new_s[::-1]
