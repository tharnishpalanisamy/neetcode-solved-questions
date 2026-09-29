class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2 :
            return max(nums)
        part1 = nums[:-1] 
        part2 = nums[1:]  

        n = len(nums) 
        dp1 = [0] * n

        dp1[0] = part1[0] 
        dp1[1] = max(part1[0] , part1[1] ) 

        for i in range(2 , n-1 ) : 
            cur = part1[i] 
            take = cur + dp1[i-2] 
            leave = dp1[i-1] 
            dp1[i] = max(take , leave) 
        
        dp2 = [0] * n
        dp2[0] = part2[0] 
        dp2[1] = max(part2[0] , part2[1])  

        for i in range(2 , n-1) :
            cur = part2[i] 
            take = cur + dp2[i-2] 
            leave = dp2[i-1] 
            dp2[i] = max(take , leave) 

        return max(max(dp1) , max(dp2)) 
