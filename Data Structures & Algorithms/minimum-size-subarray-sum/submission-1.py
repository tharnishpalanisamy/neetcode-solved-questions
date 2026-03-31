class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float("infinity")
        l = 0 
        total = 0 
        for r in range(len(nums)) :
            total += nums[r] # 14

            if total >= target :
                while total >= target : 
                    total -= nums[l] 
                    res = min(res,r-l+1)
                    l += 1 
        return 0 if res == float("infinity") else res