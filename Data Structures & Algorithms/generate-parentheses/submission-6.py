class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = [] 
        
        def backtrack(opn , close):
            if opn == close == n :
                res.append("".join(stack))
                return
            if opn < n :
                stack.append("(")
                backtrack(opn+1,close)
                stack.pop()
            if opn > close  :
                stack.append(")")
                backtrack(opn,close+1)
                stack.pop()
         
        backtrack(0,0)
        return res