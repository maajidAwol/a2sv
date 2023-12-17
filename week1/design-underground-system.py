class UndergroundSystem:

    def __init__(self):  
        self.check_in = defaultdict(list)
        self.start_to_end = defaultdict(int)
        self.start_to_end_count = defaultdict(int)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id].append(stationName)
        self.check_in[id].append(t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id].append(stationName)
        self.check_in[id].append(t)
        key = self.check_in[id][0] + "->" + self.check_in[id][2]
        self.start_to_end[key] += (self.check_in[id][3] -self.check_in[id][1])
        self.start_to_end_count[key] +=1
        self.check_in.pop(id)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + "->" + endStation 
        return self.start_to_end[key]/self.start_to_end_count[key]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)