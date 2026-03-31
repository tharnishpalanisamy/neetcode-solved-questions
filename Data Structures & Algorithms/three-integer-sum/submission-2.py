class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    n = [nums[i], nums[j], nums[k]]
                    if nums[i]+nums[j]+nums[k] == 0:
                        res.add(tuple(n))
        return [list(i) for i in res]