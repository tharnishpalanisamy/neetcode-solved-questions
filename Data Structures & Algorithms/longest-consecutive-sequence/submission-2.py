class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        seen = set(nums)
        for n in nums:
            length = 0
            if n-1 in seen:
                continue
            while n+length in seen:
                length += 1
            longest = max(length,longest)
        return longest