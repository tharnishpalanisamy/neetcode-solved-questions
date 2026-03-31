class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums: #[-1,2,-3,2]
            if nums.count(i) > 1:
                return True
        return False