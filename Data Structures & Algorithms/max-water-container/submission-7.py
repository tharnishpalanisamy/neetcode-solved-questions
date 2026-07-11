class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1 
        res = 0 

        while l < r :
            if heights[l] > heights[r] :
                current = min(heights[l],heights[r]) * (r-l )
                r -= 1 
            else :
                current = min(heights[l],heights[r]) * (r-l )
                
                l += 1 
            res = max(res,current)
        return res
