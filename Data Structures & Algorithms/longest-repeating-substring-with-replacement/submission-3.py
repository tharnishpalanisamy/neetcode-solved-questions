class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        res = 0 
        count = {}

        for r in range(len(s)):#ABBA
            count[s[r]] = count.get(s[r],0) + 1
            length = r - l + 1
            maxc = max(count.values())
            if length - maxc <= k :
                res = max(res,length)
            else:
                count[s[l]] -= 1
                l += 1
        return res

