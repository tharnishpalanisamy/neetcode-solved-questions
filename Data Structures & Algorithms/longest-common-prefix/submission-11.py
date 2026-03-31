class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]   #strs=["bat","bag","bank","band"]
        for word in strs :
            if len(prefix) > len(word):
                prefix = word # bat 
        for word in strs : #bat , bag 
            l = len(prefix)  #3
            while word[:l] != prefix :
                prefix = prefix[:-1] 
                l -= 1
                if len(prefix) == 0 :
                    break
        return prefix