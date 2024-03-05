class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        buc = []
        all_member = set()
        def sub(curr):
            if curr == len(nums):
                if tuple(sorted(buc)) not in all_member:
                    ans.append(buc[::])
                    all_member.add(tuple(sorted(buc[::])))
                return
            buc.append(nums[curr])
            sub(curr+1)
            buc.pop()
            sub(curr+1)
        sub(0)
        return ans  