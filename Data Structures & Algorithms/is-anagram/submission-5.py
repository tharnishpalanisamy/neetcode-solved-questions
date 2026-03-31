class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        for letter in s:
            s1[letter] = s1.get(letter,0)+1
        t1={}
        for letter in t:
            t1[letter] = t1.get(letter,0)+1
        return s1 == t1