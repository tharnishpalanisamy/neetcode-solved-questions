class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = [] 
        for op in operations : #ops=["5","-2","4","C","D","9","+","+"]   27
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "C" :
                stack.pop()
            elif op == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))
        return sum(stack)