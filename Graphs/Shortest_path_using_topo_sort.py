#User function Template for python3
from collections import defaultdict
from typing import List

class Solution:
    def topoSort(self,node,adj,vis,stack):
        vis[node]=1
        for i in adj[node]:
            v = i[0]
            if not vis[v]:
                self.topoSort(v,adj,vis,stack)
        stack.append(node)
        
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
    # step 1: create an adjacency list 
        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
    
        stack = []
        vis = [0]*n
        for i in range(n):
            if not vis[i]:
                self.topoSort(i,adj,vis,stack)
        
        # step 2: create a distance array and take out stack value one by one 
        dist = [float('inf')]*n
        # mention the source dist to be zero
        dist[0]=0
        while stack:
            node = stack.pop()
            for i in adj[node]:
                v,w = i
            # now perform relaxation
                if dist[node]+w <dist[v]:
                    dist[v]=dist[node]+w
        for i in range(n):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist        
                
            
        
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends
