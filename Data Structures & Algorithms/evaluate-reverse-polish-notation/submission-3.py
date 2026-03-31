class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"*":lambda x,y:x*y , "+":lambda x,y:x+y,"-":lambda x,y:x-y,"/":lambda x,y:int(x/y)}
        for i in tokens:
            if i not in ops:
                stack.append(int(i))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(ops[i](n1,n2))
        return stack[-1]
                

            
        