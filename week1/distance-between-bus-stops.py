class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # if start> destination:
        #     return min(sum(distance[destination:start]), (sum(distance[start:])+ sum(distance[:destination])))
        # return min(sum(distance[start:destination]),sum(distance[destination:len(distance)]))
        if start >  destination:
            return min(sum(distance[destination:start]),sum(distance)-sum(distance[destination:start]))
        else:
            return min(sum(distance[start:destination]),sum(distance)-sum(distance[start:destination]))