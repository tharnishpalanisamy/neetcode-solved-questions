class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [] 
        heapq.heapify(heap) 

        for p in points :
            distance = (((p[0] **2) )+ (p[1]**2))**0.5 

            heapq.heappush(heap,[distance,[p[0],p[1]]]) 
        
        res= [] 
        while len(res) < k :
            dummy = heapq.heappop(heap) 
            values = dummy[1] 
            res.append(values) 
        return res