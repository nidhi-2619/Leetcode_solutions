class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)

        indegree = [0]*numCourses
        for i in range(numCourses):
            for node in adj[i]:
                indegree[node]+=1

        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res = 0
        while q:
            node = q.popleft()
            res+=1
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        if res==numCourses:return True
        return False                                
