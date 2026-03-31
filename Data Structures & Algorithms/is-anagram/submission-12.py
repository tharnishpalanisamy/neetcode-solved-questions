class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 , t1 = [0] * 26 , [0] * 26 
        for c in s :
            key = ord(c) - 97 
            s1[key] += 1 

        for c in t :
            key = ord(c) - 97 
            t1[key] += 1 

        return s1 == t1