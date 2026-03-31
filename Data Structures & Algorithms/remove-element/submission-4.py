class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l , r = 0 , len(nums) - 1 
        k = 0
        while l < r :
            while nums[l] != val and l < r:
                l += 1
            while nums[r] == val and r > l :
                r-= 1 
            nums[l],nums[r] = nums[r] , nums[l] 
            l+= 1
            r-= 1
        for n in nums :
            if n != val :
                k += 1
        return k

                