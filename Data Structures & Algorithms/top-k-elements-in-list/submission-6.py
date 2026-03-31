class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        res = []
        bucket = [[] for i in range(len(nums)+1)]
        for num,freq in count.items():
            bucket[freq].append(num)
        for i in range(len(nums) , 0 ,-1):
            for n in bucket[i] :
                res.append(n)
                if len(res) == k:
                    return res

