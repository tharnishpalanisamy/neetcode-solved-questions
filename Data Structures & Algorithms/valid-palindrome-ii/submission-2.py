class Solution:
    def validPalindrome(self, s: str) -> bool:
        l , r = 0 , len(s) - 1 
        while l < r : # bbd   l = 1 r = 3            
            if s[l] != s[r] :
                if s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r:][::-1] :
                    return True
                return False
            l += 1
            r -= 1
        return True