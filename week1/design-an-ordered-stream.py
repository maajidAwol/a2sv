class OrderedStream:

    def __init__(self, n: int):
        self.strings = [""]*n
        self.index= 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        back = []
        self.strings[idKey-1] = value
        if not self.strings[self.index]:
            pass
        else:
            while self.index < len(self.strings)  and self.strings[self.index]:
                back.append(self.strings[self.index])
                self.index +=1 
        
        return back
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)