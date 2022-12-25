class Solution:
    def solve(self,col,n,ans,board,leftRow,upperDiagonal,lowerDiagonal):
        # base case
        if col==n:
            ans.append(["".join(r) for r in board])
        # looping through row to check if we can put the queen or not
        for row in range(n):
            if leftRow[row] == False and upperDiagonal[row+col] == False and lowerDiagonal[n-1+col-row] == False:
                board[row][col]='Q'
                leftRow[row]=True
                upperDiagonal[row+col] =True
                lowerDiagonal[n-1+col-row]=True
                #  going for next col
                self.solve(col+1,n,ans,board,leftRow,upperDiagonal,lowerDiagonal)  
                #  backtracking step now put
                board[row][col]='.'
                leftRow[row]=False
                upperDiagonal[row+col] = False
                lowerDiagonal[n-1+col-row] = False

    def solveNQueens(self, n: int) -> List[List[str]]:
        # striver  
        # declare a list to store the board
        ans = []
        # declare the board row
        board = [["."] * n for _ in range(n)]
        # left row , upper diagonal, lower diagonal
        leftRow = [False  for _ in range(n)]
        # why we have taken the size as 2*n-1
        # because row+column = diagonal 
        upperDiagonal= [False for _ in range(2*n-1)]
        lowerDiagonal=[False for _ in range(2*n-1)]
        self.solve(0,n,ans,board,leftRow,upperDiagonal,lowerDiagonal)
        return ans
