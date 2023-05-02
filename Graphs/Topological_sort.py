# GeeksForGeeks Question
class Solution:
    
    #Function to return list containing vertices in Topological order.
    def dfs(self,node,vis,adj,stack):
        vis[node]=1
        for i in adj[node]:
            if not vis[i]:
                self.dfs(i,vis,adj,stack)
        stack.append(node)
        
    def topoSort(self, V, adj):
        # Code here
        vis = [0]*V
        stack = []
        for i in range(V):
            if not vis[i]:
                self.dfs(i,vis,adj,stack)
        res = []
        while stack:
            res.append(stack[-1])
            stack.pop()
        return res    

