class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate elements
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]

                if summ == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    l += 1
                    r -= 1

                    # Skip duplicate numbers for l and r
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif summ < 0:
                    l += 1
                else:
                    r -= 1

        return res
