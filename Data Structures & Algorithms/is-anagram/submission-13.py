class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = [0] * 26 
        count2 = [0] * 26 
        for c in s :
            val = ord(c) - 97 
            count1[val] += 1 
        for c in t : 
            val = ord(c) - 97 
            count2[val]  += 1 
        return count1 == count2