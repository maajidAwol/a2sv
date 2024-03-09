class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n= len(nums)
        prefix = [0]*(n+1)
        ans = [0]*n
        for i in range(n):
            prefix[i+1] = nums[i] +prefix[i]
        for i in range(n):
            right = n-i-1
            l = nums[i]*i
            r = nums[i]*right
            ans[i] = (l-prefix[i]) + ((prefix[-1]-prefix[i+1])-r) 
        return ans
        