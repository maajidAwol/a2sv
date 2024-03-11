class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        col=[set() for _ in range(9)]
        for i in range(9):
            if i==0 or  i ==3 or i==6:
                set_1 = set()
                set_2 = set()
                set_3 = set()
            set_row= set()
            for j in range(9):
                val = ""
                if board[i][j] !="." :
                    if board[i][j] not in col[j] and board[i][j] not in set_row:
                        if 0 <= j <3 and board[i][j] not in set_1:   
                            set_1.add(board[i][j])   
                        elif 3 <= j <6 and board[i][j] not in set_2:
                            set_2.add(board[i][j])
                        elif 6 <= j <9 and board[i][j] not in set_3:
                            set_3.add(board[i][j])
                        else:
                            return False
                    else:
                        return False
                    
                    set_row.add(board[i][j])
                    col[j].add(board[i][j])
        return True