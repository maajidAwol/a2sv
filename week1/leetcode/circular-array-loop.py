class Solution:
    def circularArrayLoop(self, nums):
        n=len(nums)
        for i in range(len(nums)):
            fast = i
            par = 1 if nums[i] >0 else -1
            check =0
            while check <n:
                check +=1
                if (nums[fast] >0 and par ==-1) or (nums[fast] <0 and par == 1):
                    break
                if fast == (fast + nums[fast])%n:
                    break
                fast += nums[fast]
                fast %=n
                if fast == i:
                    return True
        return False