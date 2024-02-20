class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        for i in range(len(nums)-1):
            idx = max(idx-1,nums[i])
            if idx == 0:
                return False
        return True
            
