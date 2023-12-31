class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        sumed = 0
        for cost in costs:
            sumed +=cost
            if sumed <= coins:
                count +=1
            else:
                break
        return count