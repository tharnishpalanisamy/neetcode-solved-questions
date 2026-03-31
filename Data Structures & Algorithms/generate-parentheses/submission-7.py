class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] 

        def backtrack(openCount , closeCount,path) : 
            if openCount == closeCount == n :
                res.append("".join(path)) 
                return
            if openCount < n : 
                backtrack(openCount+1 , closeCount , path+"(")  
            if closeCount < openCount :
                backtrack(openCount , closeCount+1 , path + ")")

        backtrack(0,0,"") 
        return res