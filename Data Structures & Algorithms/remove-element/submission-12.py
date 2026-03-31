class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0 
        for r in range(len(nums)) :
            if nums[l] != val :
                l += 1 
                continue 
            if nums[r] != val :
                nums[l],nums[r] = nums[r] , nums[l] 
                l += 1
        return len(nums[:l])