class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         ans = [0]*n
#         for i in range(n):
#             l =i+1
#             r =  n-1
#             minimum = float("inf")
#             while l < r:
#                 minimum =min(abs(minimum-target),abs((nums[i]+nums[r]+nums[i])-target))
#                 l+=1
#                 r-=1
#             ans[i]=minimum
#         return ans
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return closest_sum

        return closest_sum
