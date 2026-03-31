class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs :
            length = len(word) 
            res += str(length) +"#"+ word   #4neet
        return res

    def decode(self, s: str) -> List[str]: #4#neet4#code4#love3#you 
        res = [] 
        i = 0 
        while i < len(s) :
            w = i
            while s[w] != "#" :
                w += 1 
            length = int(s[i:w])
            word = s[w+1:w+1+length] 
            res.append(word) 
            i = w+1+length
        return res
            




