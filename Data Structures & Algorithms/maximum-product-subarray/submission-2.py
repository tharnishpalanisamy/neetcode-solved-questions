class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = nums[0] 
        min_val = nums[0] 
        res = nums[0] 

        for i in range(1 , len(nums)) :
            val = nums[i] 
            new_max = max(val , max_val * val , min_val * val ) 
            res = max(res , new_max ) 
            new_min = min(val , max_val * val , min_val * val ) 

            max_val = new_max 
            min_val = new_min 
        return res