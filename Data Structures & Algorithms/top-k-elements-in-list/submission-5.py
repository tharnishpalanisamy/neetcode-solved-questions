class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        seen = []
        for num , frq in freq.items():
            seen.append([frq,num])
        seen.sort()
        res = []
        for i in range(k):
            res.append((seen.pop())[1])
        return res
