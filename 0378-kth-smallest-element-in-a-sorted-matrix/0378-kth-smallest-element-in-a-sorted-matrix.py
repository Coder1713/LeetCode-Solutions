import heapq
class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        heap=[]
        n=len(matrix)
        for i in range(n):
            heapq.heappush(heap,(matrix[i][0],i,0))
        for _ in range(k):
            val,row,col=heapq.heappop(heap)
            if(col<n-1):
                heapq.heappush(heap,(matrix[row][col+1],row,col+1))
            
        return val
            
