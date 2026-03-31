class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = [0] * 26 
        c2 = [0] * 26  

        for c in s1 :
            key = ord(c) - 97 
            c1[key] += 1 
        
        l = 0 

        for r in range(len(s2)) :
            key = ord(s2[r]) - 97 
            c2[key] += 1 
            if (r-l+1) > len(s1) :
                c2[ord(s2[l])-97] -= 1 
                l += 1 

            if c1 == c2 :
                return True 
            
        return False
        
