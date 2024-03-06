class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x+1
        while l +1  < r:
            mid = (l+r)//2
            if mid *mid == x:
                return mid
            elif mid *mid >x:
                r = mid
            else:
                l = mid
        return l