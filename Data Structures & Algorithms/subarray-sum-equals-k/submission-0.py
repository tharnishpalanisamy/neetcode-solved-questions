class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = {0:1} 
        current = 0 
        for n in nums :
            current += n 
            diff = current - k 
            res += prefix.get(diff,0) 
            prefix[current] = prefix.get(current,0) + 1 
        return res
