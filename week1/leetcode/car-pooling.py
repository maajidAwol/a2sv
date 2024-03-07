class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_ = max(trips,key = lambda x: x[2])[2]
        ans = [0]*(max_+2)
        for i in range(len(trips)):
            ans[trips[i][1]+1] +=trips[i][0]
            ans[trips[i][2]+1] -= trips[i][0]
        for j in range(1,len(ans)):
            ans[j] = ans[j-1] +ans[j]
            if ans[j] >capacity:
                return False
        return True

# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         ans = [0]*1001
#         for i in range(len(trips)):
#             ans[trips[i][1]] +=trips[i][0]
#             ans[trips[i][2]] -= trips[i][0]
#         for j in range(len(ans)):
#             ans[j] = ans[j-1] +ans[j]
#             if ans[j] >capacity:
#                 return False
#         return True
