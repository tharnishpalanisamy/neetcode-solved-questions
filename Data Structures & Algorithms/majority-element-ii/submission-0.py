class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums) 
        res = []
        for n in counter :
            if counter[n] > len(nums)/3:
                res.append(n)
        return res