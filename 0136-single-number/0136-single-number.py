class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result =0 
        for num in nums:
            result ^= num
        return result
        #return functools.reduce(operator.xor,nums,0)
        