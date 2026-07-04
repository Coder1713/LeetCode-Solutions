class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        outdegree=[0]*n
        adj={i:[] for i in range(n)}
        for u in range(n):
            for v in graph[u]:
                adj[v].append(u)
        q=deque()
        topo=[]
        for u in range(n):
            for v in adj[u]:
                outdegree[v]+=1
        for i in range(n):
            if(outdegree[i]==0):
                q.append(i)
        while q:
            node=q.popleft()
            for neigh in adj[node]:
                outdegree[neigh]-=1
                if(outdegree[neigh]==0):
                    q.append(neigh)
            topo.append(node)
        return sorted(topo)
            