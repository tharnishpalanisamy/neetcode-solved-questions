class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        p = s[0] 
        for w in s :
            if len(w) < len(p) :
                p = w 
        # p = bat 
        for w in s :
            for i in range(len(p)) : 
                if p[i] != w[i] :
                    p = p[:i] 
                    break
        return p 


                
