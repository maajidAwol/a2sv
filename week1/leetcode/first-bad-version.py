# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n+1
        while l +1 < r:
            mid = (l+r)//2
            if isBadVersion(mid):
                r = mid
            else:
                l = mid
            
        return r

