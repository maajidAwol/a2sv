class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        buc =[]
        ans = set()
        def back(size,tar,val):
            if len(buc) >size or val >10:
                return
            if sum(buc) == tar and len(buc) == size:
                ans.add(tuple(buc[::]))
            buc.append(val)
            back(size,tar,val+1)
            buc.pop()
            back(size,tar,val+1)
        back(k,n,1)
        return ans