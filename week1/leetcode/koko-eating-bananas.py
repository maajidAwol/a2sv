class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count(once):
            sum_ =0
            for i in range(len(piles)):
                sum_ += math.ceil(piles[i]/once)
            return sum_
        left = 1
        right = max(piles)
        while left<=right:
            mid = (left +right)//2
            if count(mid) <= h:
                right = mid-1
            else:
                left = mid+1


        return left