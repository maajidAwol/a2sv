class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = -1
        r = len(citations)
        n =len(citations)
        while l +1 < r:
            mid = (l+r)//2
            if citations[mid] ==(n-mid):
                return citations[mid]
            if citations[mid] > (n-mid):
                r = mid
            else:
                l = mid
        pos = n -r
        return pos