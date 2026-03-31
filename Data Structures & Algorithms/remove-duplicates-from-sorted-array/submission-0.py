class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l , r = 0 , 0 
        pos = 1 

        while r < len(nums) : #[1,1,2,3,4]   [1,2,4]  len = 5    [1,2] l = 2  , r = 3 , pos = 2 
            if nums[r] != nums[l] : 
                nums[pos] = nums[r] 
                l += 1
                pos += 1
            r += 1 
        return pos