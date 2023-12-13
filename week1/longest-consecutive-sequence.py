class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count =0 
        max_count = float("-inf")
        if len(nums) ==1 or len(nums)==0:
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] ==1:
                if count ==0:
                    count = 2
                else:
                    count +=1
            elif nums[i+1]-nums[i] ==0:
                continue
            else:
                max_count =max(max_count,count)
                count =0

        max_count =max(max_count,count)
        if max_count ==0:
            return 1
        return max_count

        