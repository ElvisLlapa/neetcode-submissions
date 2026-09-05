class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()

        for n in nums:
            if n in duplicate:
                return True
            else:
                duplicate.add(n)
        #I checked every single nuber, and I never found a duplicate
        return False