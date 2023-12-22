class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        tl = 0
        tl_c = 0
        tr = 0
        tr_c =2
        bl = 2
        bl_c = 0
        br = 2
        br_c = 2
        r = len(grid)
        c = len(grid[0])
        maximum = float("-inf")
        arr = []
        while br < r and br_c < c :
            sumed = sum(grid[tl][tl_c:tr_c +1])
            sumed += grid[tl+1][tl_c+1] 
            sumed += sum(grid[bl][bl_c:br_c +1])
            arr.append(sumed)
            if tr_c != c-1:
                tl_c +=1
                tr_c +=1
                bl_c +=1
                br_c +=1
            else:
                tr +=1
                tl +=1
                br +=1
                bl +=1
                tl_c =0
                tr_c =2
                bl_c =0
                br_c =2      
        return max(arr)