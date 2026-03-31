class Solution:
    def trap(self, nums: List[int]) -> int:
        l , r = 0 , len(nums) - 1  
        leftmax , rightmax = nums[l] , nums[r] 
        res = 0 

        while l < r :
            if leftmax > rightmax :
                r -= 1
                rightmax = max(rightmax , nums[r])  
                
                res += rightmax - nums[r] 
                
            else:
                l += 1
                leftmax = max(leftmax , nums[l] ) 
                
                res += leftmax - nums[l] 
                
        return res
