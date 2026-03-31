class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        l = 0 
        r = len(nums) - k 

        while l < r :
            m = (l+r)//2 

            if x - nums[m] > nums[m+k] - x :
                l = m + 1 
            else:
                r = m 
        return nums[l:l+k]