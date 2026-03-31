class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        seen = {}
        res = 0

        for r in range(len(s)) :
            seen[s[r]] = seen.get(s[r],0) + 1  
            if ((r-l+1) - max(seen.values()) ) <= k :
                res = max(res,(r-l+1)) 
            else:
                seen[s[l]] = seen.get(s[l],0) - 1 
                l += 1 
        return res


