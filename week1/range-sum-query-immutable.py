class NumArray:

    def __init__(self, nums: List[int]):
        self.p = [0]*(len(nums)+1)
        for i in range(1,len(self.p)):
            self.p[i] = nums[i-1] + self.p[i-1]
    def sumRange(self, left: int, right: int) -> int:
        return self.p[right+1] - self.p[left]
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)