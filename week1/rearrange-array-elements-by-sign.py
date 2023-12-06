class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative =[]
        positive = []
        ans=[]
        pi=1
        ni=0
        for num in nums:
            if num> 0:
                positive.append(num)
            else:
                negative.append(num)
        parity = -1
        ans.append(positive[0])
        for i in range(1,len(nums)):
            if parity == -1:
                print(nums[i])
                ans.append(negative[ni])
                ni +=1
                parity =1
            elif parity == 1:
                print(nums[i])
                ans.append(positive[pi])
                pi+=1
                parity =-1
        return ans