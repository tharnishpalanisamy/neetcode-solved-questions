class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            a = ord('a')
            count[ord(s[i]) - a] += 1
            count[ord(t[i]) - a] -= 1
        for i in count:
            if i!= 0:
                return False
        return True
