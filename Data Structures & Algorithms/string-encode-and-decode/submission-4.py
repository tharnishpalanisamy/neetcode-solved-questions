class Solution:#leetcode 271

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        4#leet4#code  length = 4   j = 3:3+length   leet
        res = []
        i = 0 
        while i < len(s): 
            j = i 
            while s[j]!="#":
                j+=1
            length = int(s[i:j]) #leet
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res








