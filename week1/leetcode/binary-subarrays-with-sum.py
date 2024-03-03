class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = [0] *(len(nums)+1)
        count = 0
        dict_ = defaultdict(int)
        dict_[0] =1
        for i in range(len(nums)):
            prefix[i+1] = nums[i] +prefix[i]
            temp = prefix[i+1] - goal
            if temp in dict_:
                count += dict_[temp]
            dict_[prefix[i+1]] +=1       
        return count