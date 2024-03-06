class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(mid, days):
            count = 1
            sum_ =0
            for i in range(len(weights)):
                if sum_ + weights[i] > mid:
                    count +=1
                    sum_ = weights[i]
                else:
                    sum_ +=weights[i]
            return count <= days
        min_ = max(weights)-1
        max_ = sum(weights) +1
        while min_ + 1 < max_:
            mid = (min_ + max_)//2
            if check(mid, days):     
                max_ = mid
            else:
                min_ = mid 
        return max_