class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [[] for i in range(len(nums)+1)]
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0)+1
        for n,f in freq.items():
            count[f].append(n)
        res = []
        for i in range(len(nums),0,-1):
            for j in count[i]:
                if len(res) < k:
                    res.append(j)
                else:break
        return res

