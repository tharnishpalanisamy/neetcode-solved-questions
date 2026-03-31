class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1] :
            return True 
        
        for i in range(len(s)) :
            if s[:i]+s[i+1:] == (s[:i]+s[i+1:])[::-1] :
                return True 
        return False