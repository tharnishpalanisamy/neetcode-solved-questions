class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    if nums[i]+nums[j]+nums[k] == 0:
                        if [nums[i],nums[j],nums[k]] not in res:
                            res.append([nums[i],nums[j],nums[k]])
        return res