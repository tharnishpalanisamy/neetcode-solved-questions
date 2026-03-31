class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {} 
        for c in s :
            s1[c] = s1.get(c,0)+1 
        t1 = {} 
        for c in t :
            t1[c] = t1.get(c,0) + 1 
        
        return s1 == t1