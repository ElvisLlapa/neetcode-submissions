class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_duplicates = set()
        for n in nums:
            if n in no_duplicates:
                return True
            no_duplicates.add(n)
        return False
        
