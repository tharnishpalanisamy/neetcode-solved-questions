class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position,speed)] 
        stack = [] 

        for p , s in sorted(pair,reverse=True) :
            finish = (target - p) / s 

            if not stack or stack[-1] < finish :
                stack.append(finish) 
        return len(stack)