class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s) 

        dp = [1] * n 
        dp[0] = 1 

        for i in range(1 , n ) :
            for j in range(i) :
                if s[j:i+1] == s[j:i+1][::-1] :
                    dp[i] += 1  
        return sum(dp)
            