import heapq
class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        freq={}
        heap=[]
        m,n=len(mat),len(mat[0])
        for i in range(m):
            count=mat[i].count(1)
            freq[i]=(-count,-i)
            heapq.heappush(heap,freq[i])
            while len(heap)>k:
                heapq.heappop(heap)
        ans=[]
        while heap:
            count,i=heapq.heappop(heap)
            ans.append(-i)
        ans.reverse()
        return ans

        