class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        prefix = s[0] 
        for word in s :
            if len(word) < len(prefix) :
                prefix = word  #bat 
        
        for word in s :
            for i in range(len(prefix)) : 
                if prefix[i] != word[i] :
                    prefix = prefix[:i] 
                    break 
        return prefix