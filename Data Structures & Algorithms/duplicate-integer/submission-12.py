class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()#1,2
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

