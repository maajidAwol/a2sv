class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_sum =0
        
        row = [0]*len(grid)
        col = [0]*len(grid[0])
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                col[j] = max(col[j],grid[i][j])
                row[i] = max(row[i],grid[i][j])
        for i in range(len(grid)):  
            for j in range(len(grid[0])):
                temp = min(col[j],row[i])
                max_sum += (temp-grid[i][j])
        # print(max_sum)

        return max_sum