class MyStack:

    def __init__(self):
        self.que = deque()
    def push(self, x: int) -> None:
        self.que.append(x)
    def pop(self) -> int:
        return self.que.pop()
    def top(self) -> int:
        rt = self.que.pop()
        self.que.append(rt)
        return rt
    def empty(self) -> bool:
        return len(self.que) ==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()