class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1 
        while l <= r :
            m = (l+r)//2   
            #logic 
            if nums[m] == target :
                return m 
            
            if nums[l] <= nums[m] :
                if nums[m] > target and target >= nums[l] :
                    r = m - 1 
                else:
                    l = m + 1 
            elif nums[m] <= nums[r] :
                if nums[m] < target and nums[r] >= target :
                    l = m + 1 
                else:
                    r = m - 1 



        return -1


                



