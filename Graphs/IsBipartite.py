# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def dfs(self,node,col,color,graph):
        color[node]=col
        for v in graph[node]:
            if color[v]==-1:
                if not self.dfs(v,col^1,color,graph):
                    return False
            elif color[v]==col:
                return False
        return True                

    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        color = [-1] * N
        for i in range(len(graph)):
            if color[i]==-1:
                if not self.dfs(i,0,color,graph):
                    return False
        return True  
