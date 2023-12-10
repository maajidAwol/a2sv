class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        main_set = set()
        right_left = {num for num in range(left,right+1)}
        for i in range(len(ranges)):
            temp = {r for r in range(ranges[i][0],ranges[i][1]+1)}
            main_set =main_set.union(temp)
        return right_left.issubset(main_set)
