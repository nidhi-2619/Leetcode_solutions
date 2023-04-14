class Solution:
    def dfs(self,mat ,vis,r,c):
        n,m = len(mat),len(mat[0])
        vis[r][c]=1
        xx,yy=[-1,0,+1,0],[0,+1,0,-1]
        for i in range(4):
            nr,nc = r+xx[i],c+yy[i]
            if nr>=0 and nr<n and nc>=0 and nc<m and not vis[nr][nc] and mat[nr][nc]=='O':
                self.dfs(mat,vis,nr,nc)
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,m = len(board),len(board[0])
        vis = [[0]*m for i in range(n)]
        for i in range(m):
            # first row
            if not vis[0][i] and board[0][i]=='O':
                self.dfs(board,vis,0,i)
            # last row
            if not vis[n-1][i] and board[n-1][i]=='O':
                self.dfs(board,vis,n-1,i)
        for j in range(n):
            # first col
            if not vis[j][0] and board[j][0]=='O':
                self.dfs(board,vis,j,0)
            # last row
            if not vis[j][m-1] and board[j][m-1]=='O':
                self.dfs(board,vis,j,m-1)        

        # for the o's which are diff from boundary
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and board[i][j]=='O':
                    board[i][j]='X'
        return board
