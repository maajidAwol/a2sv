class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        dict_ = dict()
        n= len(nums)
        for i in range(n*2):
            idx = i%n
            while stack and nums[stack[-1]] < nums[idx]:
                dict_[stack.pop()] = idx
            stack.append(idx)
        ans =[-1]*n
        for i in range(n):
            if i in dict_:
                ans[i] = nums[dict_[i]]
        return ans
        