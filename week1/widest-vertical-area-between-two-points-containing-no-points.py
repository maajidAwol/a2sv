class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        arr = []
        for x,y in points:
            arr.append(x)
        arr.sort()
        ans = float("-inf")
        for i in range(len(arr)-1):
            ans =max(ans,arr[i+1]-arr[i])
        return ans