class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = []
        interval = (len(mat) + len(mat[0]))
        sumed = defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                sumed[r + c].append(mat[r][c])
        for i in range(interval-1):   
            if i% 2==0:
                diagonal += reversed(sumed[i])         
            else:
                diagonal +=sumed[i]
        return diagonal