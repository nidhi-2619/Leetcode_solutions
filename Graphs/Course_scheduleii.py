class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Code here
        # the dependency is 1->0 i.e 1 needs to be completed first this
        #  show the dependency of 0 on 1
        # so we will reverse the adj list
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        
        indegree = [0]*numCourses
        q = deque()
        for node in range(numCourses):
            for i in adj[node]:
                indegree[i]+=1
        
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        
        if len(topo)==numCourses:
            return topo
        return []    
