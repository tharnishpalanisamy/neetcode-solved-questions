class Solution:
    def findInMountainArray(self, target: int, ma: 'MountainArray') -> int:
        length = ma.length() 

        l , r = 1 , length - 2 
        while l <= r :
            m = (l+r)//2 
            left = ma.get(m-1) 
            mid = ma.get(m) 
            right = ma.get(m+1) 

            if left < mid < right :
                l = m  + 1 
            elif left > mid > right :
                r = m - 1 
            else:
                break 
        peak = m 

        #left 

        l , r = 0 , peak 

        while l <= r :
            m = (l+r) // 2 

            val = ma.get(m) 

            if val > target :
                r = m - 1 
            elif val < target :
                l = m + 1 
            else:
                return m 
        
        #right 

        l , r = peak , length -1 

        while l <= r :
            m = (l+r)//2 

            val = ma.get(m) 

            if val > target :
                l = m + 1 
            elif val < target :
                r = m - 1 
            else:
                return m 

        return -1 


