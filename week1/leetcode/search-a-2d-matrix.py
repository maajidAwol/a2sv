class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left= -1
        right = len(matrix)
        while left +1 < right:
            mid = (left +right)//2
            if matrix[mid][0] >target:
                right = mid
            else:
                left = mid
        row = left
        left = -1
        right = len(matrix[row])
        while left+1 < right:
            mid= (left+right)//2
            if matrix[row][mid] ==target:
                return True
            elif matrix[row][mid] > target:
                right = mid
            else:
                left= mid
        return False