class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0] *(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] +(nums[i]%2)
        count =0
        prev =0
        l =0
        for i in range(1,len(prefix)):
            if prev and prefix[i] == prefix[i-1]:
                count +=prev
            elif prefix[i] > prefix[i-1]:
                prev = 0
                while prefix[i] - prefix[l] >= k:
                    if prefix[i] - prefix[l]==k:
                        prev +=1
                    l+=1
                count +=prev
        return count