class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False  #s1 {r:2,a:2,c:2,e:1}
        s1,t1 = {},{} #s=racecar t=carrace
        for i in range(len(s)):
            s1[s[i]] = s1.get(s[i],0)+1
            t1[t[i]] = t1.get(t[i],0)+1
        return s1 == t1

