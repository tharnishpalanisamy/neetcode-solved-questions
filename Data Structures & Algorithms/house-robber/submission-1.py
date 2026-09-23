class Solution:
    def rob(self, nums: List[int]) -> int: 
        n = len(nums) 
        if n <= 2 :
            return max(nums) 
        prev2 = nums[0] 
        prev1 = max(nums[0] , nums[1] ) 

        for i in range(2 , n )  : 
            res = max( prev2 + nums[i] , prev1 )  
            prev2 = prev1 
            prev1 = res 
        return prev1