class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: abs(x[0]-x[1]),reverse = True)
        n = len(costs)
        countA = n//2
        countB = countA
        ret =0
        print(costs)
        for x,y in costs:
            if x <= y:
                if countA:
                    ret +=x
                    countA -=1
                else:

                    ret+=y
                    countB -=1
            else:
                if countB:
                    ret +=y
                    countB-=1
                else:
                    ret +=x
                    countA -=1

        return ret