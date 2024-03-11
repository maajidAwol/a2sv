class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.n = (2*(height-2) + 2*width)
        self.curr = 0
        self.x = 0
        self.y = 0
        self.dir = "East"
    def step(self, num: int) -> None:
        self.curr = (self.curr + num) % self.n
        if self.curr > 0 and self.curr < self.width:
            self.dir = "East"
            self.x = self.curr
            self.y = 0
        elif self.curr >= self.width and self.curr < (self.width + (self.height-1)):
            self.dir = "North"
            self.y = (self.curr - (self.width-1))
            self.x = self.width-1
        elif self.curr >= (self.width + (self.height-1)) and self.curr < (2*(self.width) + self.height -2):
            self.dir = "West"

            self.x = (self.width-1)-(self.curr -(self.width+self.height-2))
            self.y = self.height-1
        else:
            self.dir = "South"
            self.x = 0
            if self.curr == 0:
                self.y = 0
            else:
                self.y = (self.height-1) - (self.curr -(2*self.width+self.height-3))            
    def getPos(self) -> List[int]:
        return [self.x,self.y]
    def getDir(self) -> str:
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()