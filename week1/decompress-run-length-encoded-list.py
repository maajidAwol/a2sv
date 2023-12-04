class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        new_list =[]
        for i in range(1,len(nums)):
            if i%2 ==1:
                
                new_list +=[nums[i]]*nums[i-1]
        return new_list