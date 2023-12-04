class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_sum =0
        max_cons =0
        for i in range(len(nums)):
            if nums[i] == 0:
                max_cons= max(max_cons, num_sum)
                num_sum *=0
            else:
                num_sum+=1
                max_cons= max(max_cons, num_sum)
        return max_cons