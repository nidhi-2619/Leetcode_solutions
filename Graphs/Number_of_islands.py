
# [Question Link](https://leetcode.com/problems/number-of-islands/)  

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        vis = [[0]*m for i in range(n)]
        count=0
        def bfs(row,col,grid,vis):
            vis[row][col]=1
            q = deque()
            q.append((row,col))
            while q:
                x,y = q.popleft()
                # traverse the neighbour
                #  we cannot use this as it is for eight direction it is applicable in gfg but here we are considering 4 directions only
                for i in range(-1,2):
                    xx = x+i
                    yy = y+i
                    if xx>=0 and xx<n and grid[xx][y]=='1' and not vis[xx][y]:
                        vis[xx][y]='1'
                        q.append((xx,y))
                    if yy>=0 and yy<m and grid[x][yy]=='1' and not vis[x][yy]:
                        vis[x][yy]='1'
                        q.append((x,yy))    
                        


        for row in range(n):
            for col in range(m):
                if grid[row][col]=='1' and not vis[row][col]:
                    count+=1
                    bfs(row,col,grid,vis)
                    
        return count            
