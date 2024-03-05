class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if len(nums) ==1:
            return [nums[::]]
        for i in range(len(nums)):
            num = nums.pop(0)
            sub = self.permute(nums)
            for s in sub:
                s.append(num)
            ans.extend(sub)
            nums.append(num)
        print(ans)
        return ans
            