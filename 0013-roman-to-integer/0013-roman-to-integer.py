class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        result = 0
        prev_value = 0
        for char in s[::-1]:
            value = roman[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result
        """
        :type s: str
        :rtype: int
        """
        
        