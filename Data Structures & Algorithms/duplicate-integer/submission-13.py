class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()#1, 2, 3
        for i in nums:#[1, 2, 3, 3]
            if i in seen:
                return True
            seen.add(i)
        return False
