class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_sequence = 0

        for n in hashset:
            if (n - 1) not in hashset:
                length = 0
                
                while(n + length) in hashset:
                    length += 1
                longest_sequence = max(length, longest_sequence)
        return longest_sequence