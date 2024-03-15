class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n= len(nums)
        prefix = [0]*(n+1)
        temp = 0
        max_= float("-inf")
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
            if nums[i] >=0 and temp==-1:
                prefix[i+1] = nums[i]
                temp = 0
            elif prefix[i+1] <0:
                temp =-1
            max_ = max(max_,prefix[i+1],nums[i])
        return max_
        