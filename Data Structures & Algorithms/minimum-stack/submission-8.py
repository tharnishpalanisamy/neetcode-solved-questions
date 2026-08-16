class MinStack:

    def __init__(self):
        self.stack = [] 
        self.min = []
        

    def push(self, val: int) -> None:
        if self.min and val <= self.min[-1] or not self.min  :
            self.min.append(val) 

        self.stack.append(val) 
        

    def pop(self) -> None:
        if self.stack :
            if self.min and self.min[-1] == self.stack[-1] :
                self.stack.pop() 
                self.min.pop()
            else:
                self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min[-1] if self.min else 0
        
