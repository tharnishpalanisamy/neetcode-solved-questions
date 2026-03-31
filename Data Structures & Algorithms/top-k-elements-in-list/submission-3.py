class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        pairs = []
        for num,frq in freq.items():
            pairs.append([frq,num])
        pairs.sort()
        result = []
        while len(result) < k :
            result.append(pairs.pop()[1])
        return result