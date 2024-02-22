class RecentCounter:

    def __init__(self):
        self.count = []
        self.cnt = 0
    def ping(self, t: int) -> int:
        self.count.append(t)
        while self.count and self.count[0] < (t-3000):
            self.count = self.count[1:]
        return len(self.count)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)