class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        less_than = [0]*n
        greater_than =  [0]*n
        small = nums[0]
        great = nums[n-1]
        less_than[0] =  nums[0]
        greater_than[n-1] = nums[n-1]
        for i in range(1,n):
            less_than[i] =min(small,nums[i])
            small = less_than[i]
        for i in range(n-2,-1,-1):
            greater_than[i] = max(great,nums[i])
            great = greater_than[i]
        for i in range(n):
            if nums[i] != greater_than[i] and nums[i] != less_than[i]:
                return True
            
        return False