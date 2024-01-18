class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = [0]*(len(nums) +1)
        my_dict = defaultdict(int)
        for i in range(len(nums)):
            p[i+1] = nums[i] + p[i]
      
        count =0
        for i in range(len(nums)):  
            if p[i+1] == k:
                count+=1
            if (p[i+1] - k) in my_dict:
                count+=my_dict[p[i+1] - k]
            my_dict[p[i+1]] +=1
        return count
