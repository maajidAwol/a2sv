class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        buc = []
        ans = []
        def combSum(idx):
            if sum(buc) >target or idx == len(candidates):
                return
            if sum(buc) == target and buc not in ans:
                ans.append(buc[::])
            buc.append(candidates[idx])
            combSum(idx)
            buc.pop()
            combSum(idx+1)
        combSum(0)
        return ans

            
            
            