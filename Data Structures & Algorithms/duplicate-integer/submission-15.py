class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()#3
        for i in nums: #3
            if i in seen:
                return True
            seen.add(i)
        return False