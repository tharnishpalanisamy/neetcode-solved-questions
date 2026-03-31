class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
            return False
        s1 = {} 
        t1 = {} 
        for i in range(len(s)) :
            c1 = s[i] 
            c2 = t[i] 
            s1[c1] = s1.get(c1,0) + 1 
            t1[c2] = t1.get(c2,0) + 1
        
        return s1 == t1