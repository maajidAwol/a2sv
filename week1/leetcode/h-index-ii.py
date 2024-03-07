class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = -1
        right = len(citations)
        length =len(citations)
        while left +1 < right:
            mid = (left+right)//2
            if citations[mid] ==(length-mid):
                return citations[mid]
            if citations[mid] > (length-mid):
                right = mid
            else:
                left = mid
        pos = length - right
        return pos