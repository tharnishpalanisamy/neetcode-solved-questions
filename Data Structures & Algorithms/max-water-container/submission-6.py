class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l , r = 0 , len(heights) - 1 
        res = 0 

        while l < r :
            if heights[l] > heights[r] :
                current = min(heights[l],heights[r]) * (r-l )
                res = max(res,current)
                r -= 1 
            else :
                current = min(heights[l],heights[r]) * (r-l )
                res = max(res,current)
                l += 1 
        return res
