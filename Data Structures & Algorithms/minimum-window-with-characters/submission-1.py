class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""
        count = {}
        for i in t :
            count[i] = count.get(i,0) + 1   #x:1,y:1,z:1
        l = 0 
        res = [-1,-1]
        length = float("infinity") 
        have = 0 
        need = len(count)
        window = {}
        for r in range(len(s)):
            c = s[r] 
            window[c] = window.get(c,0) + 1
            if c in count and window[c] == count[c] :
                have += 1
            while need == have :
                if r-l+1 < length:
                    length = r-l+1
                    res = [l,r]
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
        l,r = res 
        return s[l:r+1] if length!= float("infinity") else ""
