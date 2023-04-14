class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m = len(mat),len(mat[0])
        q = deque()
        vis = [[False]*m for i in range(n)]
        dis = [[0]*m for j in range(n)]
        for r in range(n):
            for c in range(m):
                if mat[r][c]==0:
                    vis[r][c]=True
                    q.append((r,c,0))
                    
        while q:
            row,col,dist = q.popleft()
            xx = [-1,0,+1,0]
            yy = [0,+1,0,-1]
            dis[row][col] = dist
            for i in range(4):
                nr,nc = row+xx[i],col+yy[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and not vis[nr][nc] and mat[nr][nc]==1:
                    vis[nr][nc]=True
                    q.append((nr,nc,dist+1))
        return dis                                
