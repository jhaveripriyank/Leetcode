class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Convert list to a set for O(1) lookups
        max_length = 0

        for num in num_set:
            # Check if `num` is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # Extend the sequence as far as possible
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                # Update the maximum sequence length
                max_length = max(max_length, current_length)

        return max_length