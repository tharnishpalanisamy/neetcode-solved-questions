class Solution:
    def longestPalindrome(self, s: str) -> str: 

        if s == s[::-1] :
            return s 
        n =len(s) 
        res = "" 
        length = 0 
        for i in range(n) :
            for j in range(i , n ) : 
                word = s[i:j+1] 
                if len(word) > length :  
                    if word == word[::-1] : 
                        res = word 
                        length = len(word)
        return res

        # dp = [""] * n 

        # for i , c in enumerate(s) :
        #     cur = dp[i] + c 
        #     dp[i] += c if cur == cur[::-1] else dp[i] 

        # n = 0 
        # res = ""
        # for word in dp :
        #     if len(word) > n :
        #         res = word 
        #         n = len(word) 
        # return res