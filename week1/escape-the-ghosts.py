class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        min_ghost =  float("+inf")
        for num in ghosts:
            temp = abs(num[0] -target[0]) + abs(num[1] -target[1])
            min_ghost = min(min_ghost,temp)
        my_dist = abs(0 -target[0]) + abs(0 -target[1])
        return my_dist <min_ghost