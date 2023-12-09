class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        check= 0
        for x in range(len(nums)):
            if int(nums[x] ) != check:
                return check
            check +=1
        return check
        