import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap=[]
        for x in stones:
            heapq.heappush(heap,-x)
        while len(heap)>1:
            y=heapq.heappop(heap)
            x=heapq.heappop(heap)
            if(x!=y):
                heapq.heappush(heap,y-x)
        if not heap:
            return 0
        return -heap[0]
