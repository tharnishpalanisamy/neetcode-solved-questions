class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""
        l = 0 
        have = 0 
        t1 = Counter(t) 
        need = len(t1) 
        res = [-1,-1] 
        resl = float("infinity") 
        count = {} 
        for r in range(len(s)) :
            c = s[r] 
            count[c] = count.get(c,0) + 1 

            if c in t1 and count[c] == t1[c] :
                have += 1 
            
            while have == need :
                if resl > r-l+1 :
                    res = [l,r] 
                    resl = r-l+1
                count[s[l]] -= 1 
                if s[l] in t1 and count[s[l]] < t1[s[l]] :
                    have -= 1 
                l += 1 
        l,r = res
        return s[l:r+1] if resl != float("infinity") else ""
