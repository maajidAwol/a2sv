class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        buc =[]
        ans = []
        def back(curr):
            if len(buc) ==k:
                ans.append(buc[::])
                return
            
            for j in range(curr+1,n+1):
                buc.append(j)
                back(j)
                buc.remove(j)
        back(0)
        return ans