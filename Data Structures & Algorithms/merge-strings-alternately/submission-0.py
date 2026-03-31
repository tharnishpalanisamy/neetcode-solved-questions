class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 , l2 = 0,0 
        r1,r2 = len(word1) , len(word2)
        res = "" 
        
        while l1 < r1 and l2 < r2 : 
            res = res + word1[l1] + word2[l2]
            l1 += 1
            l2 += 1 
        while l1 < r1 :
            res += word1[l1] 
            l1 += 1
        while l2 < r2 :
            res += word2[l2] 
            l2 += 1
        return res