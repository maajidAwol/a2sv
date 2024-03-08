class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        element = len(set(nums))   
        count =0
        for i,num in enumerate(nums):
           set_ =set()
           set_.add(nums[i])
           for j in range(i,len(nums)):
               set_.add(nums[j])
               if len(set_) >= element:
                   count +=1
        return count 
            
