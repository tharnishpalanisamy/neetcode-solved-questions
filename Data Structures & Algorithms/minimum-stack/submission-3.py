class MinStack:

    def __init__(self):
        self.items = []
        self.small = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.small or self.small[-1] >= val:
            self.small.append(val)

    def pop(self) -> None:
        if self.small[-1] == self.items[-1]:
            self.small.pop()
        if self.items : self.items.pop()
        
        

    def top(self) -> int:
        if self.items:
            return self.items[-1]
        

    def getMin(self) -> int:
        if self.small : return self.small[-1]
        
