class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #  we will use bfs as it requires minimum time to rotten all the fresh oranges
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for i in range(n)]
        maxtime = 0
        count,cntFresh = 0,0
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    vis[i][j]==2
                    q.append((i,j,0))
                if grid[i][j]==1:
                    vis[i][j]=1
                    cntFresh+=1
        rr = [-1,0,+1,0]
        cc = [0,+1,0,-1]
        while q:
            r,c,t = q.popleft()
            maxtime = max(maxtime,t)
            # check its neighbour
            for i in range(4):
                nr = r+rr[i]
                nc = c+cc[i]
                if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]==1 and vis[nr][nc]==1:
                    q.append((nr,nc,t+1))
                    vis[nr][nc]=2
                    count+=1
        if count!=cntFresh:return -1
        return maxtime            


