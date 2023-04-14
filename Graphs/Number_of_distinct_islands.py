import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self,r,c,grid,vis,ans,baser,basec):
        n=len(grid)
        m = len(grid[0])
        xx = [-1,0,+1,0]
        yy = [0,+1,0,-1]
        vis[r][c]=1
        ans.append((r-baser,c-basec))
        for i in range(4):
            nr = r+xx[i]
            nc = c+yy[i]
            if nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]==1 and not vis[nr][nc]:
                self.dfs(nr,nc,grid,vis,ans,baser,basec)
        
            
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        n = len(grid)
        m = len(grid[0])
        vis = [[0]*m for i in range(n)]
        s = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and not vis[i][j]:
                    val = []
                    # row,col,grid,vis,base row,base col
                    self.dfs(i,j,grid,vis,val,i,j)
                    s.add(tuple(val))
        return len(s)   
