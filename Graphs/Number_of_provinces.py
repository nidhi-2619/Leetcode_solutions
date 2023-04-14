class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis = [0 for i in range(len(isConnected)+1)]
        # change the adjaceny matrix to adjaceny list
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1 and i!=j:
                    graph[i].append(j)
                    graph[j].append(i)
        # no of provinces
        count = 0
        def dfs(node):
            vis[node]=1
            for i in graph[node]:
                if not vis[i]:
                    dfs(i)

        for i in range(len(isConnected)):
            if not vis[i]:
                count+=1
                dfs(i)
        return count

