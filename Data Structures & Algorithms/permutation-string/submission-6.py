class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {} #a:1,b : 1 
        for i in s1: 
            count[i] = count.get(i,0) + 1
        l = 0 
        temp = {} # l : 1 , e: 1
        for r in range(len(s2)): #"lecabee"  ab
            temp[s2[r]] = temp.get(s2[r] , 0 ) + 1
            word = s2[l:r+1]
            if (r-l + 1) >= len(s1):
                if count == temp :
                    return True
                if temp[s2[l]] > 1 :
                    temp[s2[l]] -= 1
                else:
                    temp.pop(s2[l],None)
                l+= 1 
        return False
