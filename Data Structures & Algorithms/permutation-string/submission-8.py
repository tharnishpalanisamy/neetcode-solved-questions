class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        c1 = [0] * 26 
        for c in s1 :
            key = ord(c) - 97 
            c1[key] += 1 

        l = 0 
        for r in range(len(s1)-1,len(s2)) :
            c2 = [0] * 26 
            for c in s2[l:r+1] :
                key = ord(c) - 97 
                c2[key] += 1 
            if c1 == c2 :
                return True
            l += 1 
        return False