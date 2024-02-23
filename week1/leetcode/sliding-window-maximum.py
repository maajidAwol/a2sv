class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        qu= deque()
        qu.append(0)
        for i in range(len(nums)):
            if (i - qu[0]) == k:
                qu.popleft()
            while qu and nums[qu[-1]] <=  nums[i]:
                qu.pop()
            qu.append(i)
            if i+1 >= k:
                ans.append(nums[qu[0]])
        return ans


         