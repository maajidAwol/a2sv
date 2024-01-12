class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = 0
        zero =0
        l=0
        for i in range(l,len(nums)):
            if nums[i]==0:     
                zero +=1
                if zero >=2:
                    while nums[l] != 0:
                        l+=1
                    l+=1
                    zero -=1
            maximum =max(maximum,(i-l))
        return maximum
                
