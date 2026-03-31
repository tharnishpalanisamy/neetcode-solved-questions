class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:  #a:1,d:1,c:1 
            count[i] = count.get(i,0) + 1
        l = 0 
        for r in range(len(s1)-1,len(s2)): # 3 , 4
            word = s2[l:r+1]
            temp = {}
            for letter in word :
                temp[letter] = temp.get(letter,0) + 1
            if temp == count :
                return True
            l += 1
        return False
#s1="adc"  s2="dcda"