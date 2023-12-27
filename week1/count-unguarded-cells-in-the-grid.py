class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[""]* n for i in range(m)]
        for i,j in guards:
            grid[i][j] = "G"
        for i,j in walls:
            grid[i][j] = "W"
        count = 0    
        for row in range(m):
            for col in range(n):             
                r =  col +1
                l = col -1
                t = row-1
                b = row +1
                if grid[row][col] == "G":      
                    while r < n:
                        if grid[row][r] == "" or grid[row][r] == "x":
                            grid[row][r] = "x"
                        else:
                            break
                        r+=1
                    while l >=0:
                        if grid[row][l] =="" or grid[row][l] =="x":
                            grid[row][l] = "x"
                            l-=1
                        else:
                            break         
                    while t >= 0:
                        if grid[t][col] == "" or grid[t][col] == "x":
                            grid[t][col] ="x"
                        else:
                            break
                        t -=1
                    
                    while b < m:
                        if grid[b][col] ==""  or grid[b][col] =="x":
                            grid[b][col] ="x"
                        else:
                            break
                        b+=1       
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "":
                    count +=1
        return count
                
