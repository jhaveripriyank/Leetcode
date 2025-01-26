class Solution:
    def mySqrt(self, x: int) -> int:  # Added "self" as the first parameter
        if x < 2:
            return x
        for i in range(0, x//2+1):
            if i*i <= x and (i+1)**2 > x:
                return i
