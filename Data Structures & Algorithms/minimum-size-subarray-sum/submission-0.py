class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("infinity")
        l = 0 
        total = 0 
        for r in range(len(nums)) :
            total += nums[r] # 14

            if total >= target :
                res = min(res,r-l+1) #5

                while total >= target : # 12
                    total -= nums[l] # 11
                    res = min(res,r-l+1)
                    l += 1 # 2
                     # 4
        return 0 if res == float("infinity") else res