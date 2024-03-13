class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n= len(nums)
        prefix= [0]*(n+1)
        my_dict = defaultdict(int)
        my_dict[0] =1
        count =0
        for i in range(n):
            prefix[i+1] = (nums[i] +prefix[i]) %k
            if prefix[i+1] %k in my_dict:
                count +=my_dict[prefix[i+1]]
            my_dict[prefix[i+1]] +=1    
        return count