class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        buc = []
        def sub(curr):
            if curr == len(nums):
                ans.append(buc[::])
                return
            buc.append(nums[curr])
            sub(curr+1)
            buc.pop()
            sub(curr+1)
        sub(0)
        return ans