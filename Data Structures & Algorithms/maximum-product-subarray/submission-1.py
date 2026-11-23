class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 :
            return nums[0] 

        max_product = nums[0] 
        min_product = nums[0] 
        res = nums[0] 

        for i in range(1 , n ) :
            val = nums[i] 

            new_max = max(val , max_product * val , min_product * val ) 
            res = max(res , new_max) 
            new_min = min(val , max_product*val , min_product*val ) 
        
            max_product = new_max 
            min_product = new_min 
        return res
            
