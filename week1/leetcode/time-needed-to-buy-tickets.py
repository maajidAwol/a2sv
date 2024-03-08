class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        tickets = deque(tickets)
        n= len(tickets)
        count = 0
        while tickets[k] !=0 :
            temp = tickets.popleft()
            if temp:
                temp-=1
                count +=1
            tickets.append(temp)
            k=(k-1)%n          
        return count
