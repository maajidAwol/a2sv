class Solution:
    def largestNumber(self, nums: List[int]) -> str:
       if len(list(set(nums))) ==1 and list(set(nums))[0] == 0:
           return "0"
       for i in range(len(nums)):
           for j in range(i,len(nums)):
               if (str(nums[i]) + str(nums[j]) ) < (str(nums[j]) + str(nums[i]) ):
                    nums[i],nums[j] = nums[j],nums[i]
       nums = [str(num) for num in nums]
       return "".join(nums) 