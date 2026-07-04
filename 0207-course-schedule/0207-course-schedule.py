class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n=numCourses
        indegree=[0]*n
        adj={i:[] for i in range(n)}
        for a,b in prerequisites:
            adj[b].append(a)
        for u in range(n):
            for v in adj[u]:
                indegree[v]+=1
        q=deque()
        for i in range(n):
            if(indegree[i]==0):
                q.append(i)
        topo=[]
        while q:
            node=q.popleft()
            for nei in adj[node]:
                indegree[nei]-=1
                if(indegree[nei]==0):
                    q.append(nei)
            topo.append(node)
        return len(topo)==n

        