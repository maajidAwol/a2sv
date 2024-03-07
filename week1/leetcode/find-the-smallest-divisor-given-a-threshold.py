class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divide(divisor):
            sum_=0
            for i in range(len(nums)):
                sum_ += math.ceil(nums[i]/divisor)
            return sum_
        l = 1
        r = sum(nums)
        if r <= threshold:
            return 1
        while l <=r:
            mid = (l+r)//2
            if divide(mid) <= threshold:
                r = mid-1
            else:
                l = mid+1
        return l