class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rt=[]
        i=0
        while i < len(nums)-1:
            j=i+1
            while j <len(nums):
                if nums[i]+nums[j] == target:
                    rt.append(i)
                    rt.append(j)
                    break
                j+=1
            i +=1
        return rt
        