class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        grid = [list(string) for string in strs]
        transpose = [[""]*len(grid) for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                transpose[j][i] = grid[i][j]
                
        count = 0
        for i in range(len(transpose)):
            if sorted(transpose[i]) != transpose[i]:
                count +=1
        return count