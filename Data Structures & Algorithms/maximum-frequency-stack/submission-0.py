class FreqStack:

    def __init__(self):
        self.count = {}  #normal frequnecy count
        self.maxc = 0 
        self.stack = {} # frequency : numbers  1:1,2,3,4 , 2:1,2,3   3:1,2 
        

    def push(self, val: int) -> None:
        valCount = self.count.get(val,0) + 1 
        self.count[val] = valCount
        if valCount > self.maxc :
            self.maxc = valCount 
            self.stack[valCount] = [] 
        self.stack[valCount].append(val) #1:val 
        

    def pop(self) -> int:
        res = self.stack[self.maxc].pop() 
        self.count[res] -= 1 
        if not self.stack[self.maxc] :
            self.maxc -= 1 
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()