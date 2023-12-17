class Bitset:

    def __init__(self, size: int):
        self.set0 = {bit for bit in range(size)}
        self.set1 = set()
    def fix(self, idx: int) -> None:
        self.set0.discard(idx)
        self.set1.add(idx)
    def unfix(self, idx: int) -> None:    
        self.set1.discard(idx)
        self.set0.add(idx)
    def flip(self) -> None:
        temp = self.set0
        self.set0 =self.set1
        self.set1 = temp
    def all(self) -> bool:
        if not self.set0:       
            return True
        else:
            return False
    def one(self) -> bool:
        if self.set1:
            return True
        else:
            return False
    def count(self) -> int:
        return len(self.set1)
    def toString(self) -> str:
        bitString = [""]*(len(self.set0) +len(self.set1))
        list1=list(self.set1)
        list0=list(self.set0)
        for i in list1:
            bitString[i] = "1"
        for i in list0:
            bitString[i] = "0"
        return "".join(bitString)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()