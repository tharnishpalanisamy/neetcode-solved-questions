class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] 

        for p in points :
            distance = (p[0]**2) + (p[1]**2) 
            minHeap.append([distance,p[0],p[1]]) 
        heapq.heapify(minHeap) 

        res = [] 
        while len(res) < k :
            d,p1,p2 = heapq.heappop(minHeap) 
            res.append([p1,p2]) 
        return res