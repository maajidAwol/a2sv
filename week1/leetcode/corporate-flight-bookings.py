class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+2)
        for i in range(len(bookings)): 
            ans[bookings[i][0]] +=bookings[i][2]
            ans[bookings[i][1] +1] -= bookings[i][2]
        for j in range(1,len(ans)):
            ans[j] = ans[j-1] + ans[j]
        return ans[1:n+1]