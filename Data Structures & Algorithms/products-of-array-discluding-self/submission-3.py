class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        l = len(nums)
        res = [1] * l
        for i in range(l):
            res[i] = prefix
            prefix *= nums[i]
        for i in range(l):
            res[l-1-i] *= suffix
            suffix *= nums[l-1-i]  
        return res      