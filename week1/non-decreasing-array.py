class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        check_list = nums.copy()
       
        if len(nums) <=2 or nums == sorted(nums):
            
            return True
        for i in range(1,len(nums)):
            check_list = nums.copy()
            if i == len(nums)-1 and nums[i] < nums[i-1]:
          
                check_list.pop(i)
                return check_list == sorted(check_list)
            elif nums[i] < nums[i-1] and nums[i-1] > nums[i+1]:
                check_list.pop(i-1)
                
                return check_list == sorted(check_list)
            elif  nums[i] < nums[i-1] and nums[i-1] <= nums[i+1]:
                check_list.pop(i)
                return check_list == sorted(check_list)   
        return False