class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n=len(graph)
        color=[-1]*n
        q=deque()
        def bfs(start):
            q.append(start)
            color[start]=0
            while q:
                node=q.popleft()
                for neigh in graph[node]:
                    if color[neigh]==-1:
                        color[neigh]=1-color[node]
                        q.append(neigh)
                    else:
                        if(color[neigh]==color[node]):
                            return False
            return True        
        for i in range(n):
            if color[i]==-1:
                if not bfs(i):
                    return False
        return True