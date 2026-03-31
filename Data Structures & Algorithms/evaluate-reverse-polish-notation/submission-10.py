class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 
        ops = {"+":lambda x, y : int(x) + int(y) ,
        "-":lambda x, y : int(x) - int(y) ,
        "*":lambda x, y : int(x) * int(y) ,
        "/":lambda x, y : int(x/y)  }

        for c in tokens :
            if c in ops :
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(ops[c](n1,n2)) 
            else:
                stack.append(int(c))
        return stack.pop()
