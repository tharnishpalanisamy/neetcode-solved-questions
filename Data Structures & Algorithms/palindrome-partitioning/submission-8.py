class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 

        def isPalindrome(s) :
            l , r = 0 , len(s) - 1 
            while l < r :
                if s[l] != s[r] :
                    return False 
                l += 1 
                r -= 1
            return True
        
        def backtrack(index,path) :
            if index == len(s) :
                res.append(path[:])
                return 
            
            for i in range(index,len(s)) :
                if isPalindrome(s[index:i+1]) :
                    path.append(s[index:i+1]) 
                    backtrack(i+1,path) 
                    path.pop() 
        backtrack(0,[]) 
        return res
