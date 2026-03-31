class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] 
        def is_palindrome(s) :
            if s == s[::-1] :
                return True 
        path = [] 

        def backtrack(index) :
            if index >= len(s) :
                res.append(path[:]) 
                return 
            
            for i in range(index,len(s)) :
                if is_palindrome(s[index:i+1]) :
                    path.append(s[index:i+1]) 
                    backtrack(i+1) 
                    path.pop() 
        backtrack(0) 
        return res