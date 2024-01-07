class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        maximum = nums[k - 1]
        for i in range(k, len(nums)):
            maximum = max(maximum, nums[i] - nums[i - k])
        
        return maximum / k