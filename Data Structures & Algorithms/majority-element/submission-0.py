class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums :
            count[n] = count.get(n,0) + 1 

        res = 0
        majority = len(nums) / 2 
        for n in count :
            if count[n] > majority :
                res = n 
        return res
