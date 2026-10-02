import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        answer=[]
        heap=[]
        heapq.heappush(heap,1)
        for _ in range(n):
            min_num=heapq.heappop(heap)
            a=min_num*2
            b=min_num*3
            c=min_num*5
            if(a not in heap):
                heapq.heappush(heap,a)
            if(b not in heap):
                heapq.heappush(heap,b)
            if(c not in heap):
                heapq.heappush(heap,c)
        return min_num