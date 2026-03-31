class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0] * 26 
        b = [0] * 26 
        for n in s :
            key = ord(n) - 97 
            a[key] += 1 
        for n in t :
            key = ord(n) - 97 
            b[key] += 1 
        return a == b 