class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans = [0]*1001
        for i in range(len(trips)):
            ans[trips[i][1]] +=trips[i][0]
            ans[trips[i][2]] -= trips[i][0]
        for j in range(len(ans)):
            ans[j] = ans[j-1] +ans[j]
            if ans[j] >capacity:
                return False
        return True
