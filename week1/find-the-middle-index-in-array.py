class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        p = [0]*(len(nums)+1)
        for i in range(len(nums)):
            p[i+1] = p[i]+nums[i]
        for i in range(len(nums)):
            if p[i] == p[len(nums)]- p[i+1]:
                return i
        return -1