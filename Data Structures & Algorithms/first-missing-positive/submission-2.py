class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 1 
        nums.sort() 
        seen = set(nums)
        for n in nums :
            if res in seen :
                res += 1 
            else:
                return res
        return res