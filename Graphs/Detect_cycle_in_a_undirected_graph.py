# Also instead of carrying the base pointers we can alter the array after storing each coordinates in DFS call and since python wasn't allowing me to hash array values so need to convert it to tuple before storing
from typing import List
from collections import deque
class Solution:
    def detect(self,vis,adj,source):
        vis[source]=True
        q = deque()
        # (source node,parent node)
        q.append((source,-1))
        while q:
            node,parent = q.popleft()
            for i in adj[node]:
                if not vis[i]:
                    vis[i]=True
                    q.append((i,node))
                # means it is in vis and the value of node is not equal to the parent 
                # ie it has cycle
                #  parent is checking with the current node to ensure that it is not the
                #  previous node that we have visited but the new node which is already visited
                #  before this node could visit
                elif parent!=i:  
                    return True
        return False
    
    def dfs(self,vis,adj,node,parent):
        vis[node]=True
        for i in adj[node]:
            if not vis[i]:
                # if at any point it return false we get that it has cycle and we will return true
                if self.dfs(vis,adj,i,node):
                    return True
            elif i!=parent:
                return True
        return False        
        
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis = [False]*V
# 		for all components
		for i in range(V):
		    if not vis[i]:
		        if self.dfs(vis,adj,i,-1):
		            return True
		return False  
