class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (nums[i] + prefix[i]) % p 

        target = prefix[-1] % p 
        if target == 0:
            return 0  
        
        index = {}
        min_length = float('inf')
        index[0] = 0  

        for i in range(1, n + 1):
            complement = (prefix[i] - target) % p  
            if complement in index:
                min_length = min(min_length, i - index[complement])

            index[prefix[i]] = i  

        return min_length if min_length < n else -1 
        

        