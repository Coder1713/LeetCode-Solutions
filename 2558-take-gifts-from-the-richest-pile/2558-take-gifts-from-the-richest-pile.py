import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap=[]
        for gift in gifts:
            heapq.heappush(heap,-gift)
        for _ in range(k):
            a=-heapq.heappop(heap)
            b=int(a**(0.5))
            heapq.heappush(heap,-b)
        return -sum(heap)