class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0 
        r = x 
        while l <= r :
            m = (l+r)//2  #4
            value = m * m 
            if value > x :
                r = m -1 
            elif value < x :
                l = m+1
            else:
                return m 
        return r 

#  0  1  2  3  4  5  6  7  8       res = 2
#  