class Solution:
    def smallestNumber(self, num: int) -> int:
        nums = str(num)  
        nums = list(nums)
        if num >= 0:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] > nums[j]:
                        nums[i],nums[j] = nums[j],nums[i]
            if nums[0] == "0":
                for i in range(len(nums)):
                    if nums[i] > "0":
                        nums[0],nums[i] = nums[i],nums[0]
                        break       
        else:
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i] < nums[j]:
                        nums[i],nums[j] = nums[j],nums[i]
            nums = ["-"] + nums[:-1]
            
        return int("".join(nums))