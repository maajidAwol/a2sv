class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency ={}
        ans=[]
        n=len(nums)
        for i in range(len(nums)):
            if nums[i] in frequency:
                frequency[nums[i]]+=1
            else:
                frequency[nums[i]]=1
        for i,num in frequency.items():
            if frequency[i] > (n//3):
                ans.append(i)
        return ans