class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #nums = [1,2,3,4]    #[1,2,3,4]
        return len(nums) != len(set(nums))