class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 #height=[1,7,2,5,4,7,3,6]
        l = 0   #        0 1 2 3 4 5 6 7
        r = len(heights)-1
        while l < r:
            s = min(heights[l],heights[r])
            total = (r-l) * s
            if total > res : 
                res = total
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return res
            
            
            
        
