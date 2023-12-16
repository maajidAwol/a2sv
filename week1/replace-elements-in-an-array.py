class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numbers = {}
        for i,num in enumerate(nums):
            numbers[num] = i
        for key, value in operations:    
            if numbers.get(key,-1) !=-1:
                nums[numbers[key]] = value
                numbers[value]=numbers[key]
                numbers[key] = -1             
        return nums
        