class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float("inf")
        self.dict = defaultdict(int)
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.dict[val] +=1
    def pop(self) -> None:
        val = self.stack.pop()
        self.dict[val]-=1
        if self.dict[val] ==0:
            del self.dict[val]

    def top(self) -> int:
        
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.dict)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()