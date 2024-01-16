class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # running = []
        # total=0
        # for i in range(len(nums)):
        #     total +=nums[i]
        #     running.append(total)
        # return running
        for i in range(1,len(nums)):
            nums[i] +=nums[i-1]
        return nums