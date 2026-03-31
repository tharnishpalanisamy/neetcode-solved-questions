class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 

        for i,n in enumerate(nums) : #target = 7 
            diff = target - n #4 
            if diff in seen :
                return [seen[diff],i] 
            seen[n] = i 