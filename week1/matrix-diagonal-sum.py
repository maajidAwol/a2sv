class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sumed = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i-j == 0 or i+j == len(mat)-1:
                    sumed +=mat[i][j]
                    print(mat[i][j])          
        return sumed
        