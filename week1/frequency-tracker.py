class FrequencyTracker:

    def __init__(self):
       self.array =[] 
       self.tracker = defaultdict(int)
       self.frequency2 = defaultdict(int)

    def add(self, number: int) -> None:
        self.frequency2[self.tracker[number]] -=1
        self.tracker[number]+=1
        self.frequency2[self.tracker[number]] +=1

        self.array.append(number)

    def deleteOne(self, number: int) -> None:
        if number in self.array:
            self.frequency2[self.tracker[number]] -=1
            self.tracker[number]-=1
            self.frequency2[self.tracker[number]] +=1
            self.array.remove(number)
    def hasFrequency(self, frequency: int) -> bool:
        if self.frequency2[frequency] >0:
            return True
        else:
            return False



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)