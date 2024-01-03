class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        count =0
        l =0
        r = n-1
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] <target:
        #             count +=
        while l < r:
            if nums[l] + nums[r] < target:
                count +=(r-l)
                l+=1
            else:
                r-=1
        return count