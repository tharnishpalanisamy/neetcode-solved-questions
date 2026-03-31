class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        val = nums[0]   #1
        for n in nums :    #[1,2,3,2,2,2,5,4,2] 
            if val == n :
                count += 1 
            else:
                count -= 1 
            if count == 0 :
                val = n  # 2   2
                count += 1 

        return val  