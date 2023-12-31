class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        operation =0
        numed = nums.copy()
        numed = list(set(numed))
        numed.sort()
        dict_op = {}
        for i,num in enumerate(numed):
            dict_op[num] =i
        for i in range(len(nums)):
            operation +=dict_op[nums[i]]
        return operation