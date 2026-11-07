class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        def isafe(row,col,n,board):
            temp_row=row
            temp_col=col

            while col>=0 and row>=0:
                if board[row][col]=="Q":
                    return False
                col-=1
                row-=1

            row=temp_row
            col=temp_col

            while col>=0:
                if board[row][col]=="Q":
                    return False
                col-=1

            row=temp_row
            col=temp_col
            
            while col<n and row<n:
                if board[row][col]=="Q":
                    return False
                row+=1
                col-=1
            return True

        
        def nqueen(col,board,ans,n):
            if col==n:
                res=[]
                for row in board:
                    res.append("".join(row))
                ans.append(res)
                return
            for row in range(0,n):
                if isafe(row,col,n,board):
                    board[row][col]="Q"
                    nqueen(col+1,board,ans,n)
                    board[row][col]="."





        board=[]

        for i in range(n):
            board.append(["."]*n)
        
        ans=[]
        
        nqueen(0,board,ans,n)

        return ans

        