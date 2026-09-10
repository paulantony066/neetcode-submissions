class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row validation
        seen=set()
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]!="." and board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
            seen=set()
        seen=set()
        for j in range(len(board)):
            for i in range(len(board)):
                if board[i][j]!="." and board[i][j] in seen:
                    return False
                else:
                    seen.add(board[i][j])
            seen=set()
        seen=set()
        for i in range(0,9,3):
            for j in range(0,9,3):
                for n in range(3):
                    for m in range(3):
                        if board[i+n][j+m]!="." and board[i+n][j+m] in seen:
                            return False
                        seen.add(board[i+n][j+m])
                seen=set()
        return True
        
        
