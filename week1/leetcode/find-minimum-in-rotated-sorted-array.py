class Solution:
    def findMin(self, nums):
        if nums[0] <= nums[-1]:
            return nums[0]
        l = 0
        r = len(nums) - 1

        ans = nums[0]
        while l + 1 < r:
            mid = l + (r - l)//2
            if nums[mid] >= nums[l]:
                l = mid
            else:
                r = mid
        return nums[r]