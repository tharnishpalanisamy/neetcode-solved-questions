class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        l = max(nums) # 10 
        r = sum(nums) # 10 
        res = r 
        
        def canShip(cap): 
            d , curCap = 1 , cap 
            for w in nums :
                if curCap - w < 0 :
                    d += 1 
                    curCap = cap
                curCap -= w
            return True if d <= days else  False

        while l <= r :
            w = (l+r)// 2 
            if canShip(w) :
                res = min(res,w) 
                r = w - 1 
            else : 
                l =  w + 1 
        return res








        
                