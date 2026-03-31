class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        for s in strs :
            if len(s) < len(word) :
                word = s
        prefix = ""
        position = 0 
        for l in word :  # b   a   g 
            for s in strs :
                if s == "" : return ""
                if s[position] != l :
                    return prefix 
            prefix += l 
            position += 1 
        return prefix
        
