class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        values = [-x for x in stones] 

        heapq.heapify(values) 

        while len(values) > 1 :
            val1 = (heapq.heappop(values)) * -1 
            val2 = (heapq.heappop(values)) * -1  
            diff = abs(val1-val2) 
            if diff:
                heapq.heappush(values,-diff) 
        return values[0] * -1 if values else 0
