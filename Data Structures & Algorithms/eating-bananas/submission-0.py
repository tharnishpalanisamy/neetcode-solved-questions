class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        res = max(piles)  #piles=[25,10,23,4]   h = 4    out = 25
        while l<= r :
            mid = (l+r)//2 #13
            total = 0 
            for pile in piles :
                total += math.ceil(pile/mid)
            if total > h :
                l = mid + 1
            elif total <= h :
                r = mid - 1 
                res = min(mid,res)
                
        return res