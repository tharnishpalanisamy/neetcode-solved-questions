class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums)+1)] #[[],[1],[2],[3],[],[],[]]
        freq = {}  # 1:1 , 2:2,3:3 
        for n in nums:
            freq[n] = freq.get(n,0) + 1 
        
        for n in freq :
            buckets[freq[n]].append(n) 
        
        res = [] 
        for i in range(len(buckets)-1,-1,-1) :
            for n in buckets[i] :
                if len(res) < k :
                    res.append(n)
        return res
        
