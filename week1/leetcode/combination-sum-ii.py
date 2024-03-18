class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        buc = []
        ans = []
        sum_ = 0
        count = list(Counter(candidates).items())
        def combSum(idx,req,aval):
            if aval <req:
                return
            if req == 0:
                ans.append(buc[::])
                return 
            if req <0 or idx == len(count):
                return
            for i in range(count[idx][1]+1):
                buc.extend([count[idx][0]]*i)
                combSum(idx+1, req-(i*count[idx][0]),aval-(count[idx][1]*count[idx][0]))
                for _ in range(i): buc.pop()
                
        combSum(0,target,sum(candidates))
        return ans