# [Question](https://leetcode.com/problems/flood-fill/)
  
class Solution:
    def dfs(self,rr,cc,image,initial,color,ans,xx,yy):
        image[rr][cc]=color
        n=len(ans)
        m=len(ans[0])
        for i in range(4):
            nr = rr+xx[i]
            nc = cc+yy[i]
            # checking for valid condition and checking if image have same color as initial and in answer the color is not equal to the new color
            if nr>=0 and nr<n and nc>=0 and nc<m and ans[nr][nc]!=color and image[nr][nc] == initial:
                ans[nr][nc]=color
                self.dfs(nr,nc,image,initial,color,ans,xx,yy)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ans =  image.copy()
        initial = image[sr][sc]
        xx=[-1,0,+1,0]
        yy=[0,+1,0,-1]
        # now first paint the initial point or pixel to new color
        self.dfs(sr,sc,image,initial,color,ans,xx,yy)
        return ans
