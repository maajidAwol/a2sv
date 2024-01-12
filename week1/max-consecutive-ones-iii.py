class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l= 0
        maximum =0
        n= len(nums)
        for i in range(n):
            if nums[i] == 0:  
                if k==0:
                    while k ==0:
                        if nums[l] == 0:
                            k+=1
                            l+=1
                        else:
                            l+=1
                k-=1
            maximum =max(maximum,(i-l+1))        
        return maximum