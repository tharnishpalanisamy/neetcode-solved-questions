class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [] 

        def backtrack(open , close , stack) :
            if open == close == n : 
                res.append(''.join(stack))
            if open < n : 
                stack.append('(') 
                backtrack(open+1,close,stack) 
                stack.pop()
            if close < open :
                stack.append(')') 
                backtrack(open,close+1 , stack)  
                stack.pop()
        backtrack(0,0,[]) 
        return res
            