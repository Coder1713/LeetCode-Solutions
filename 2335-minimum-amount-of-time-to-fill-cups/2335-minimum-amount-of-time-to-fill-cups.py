import heapq
class Solution:
    def fillCups(self, amount: list[int]) -> int:
        time=0
        heap=[]
        for i in amount:
            if(i!=0):
                heapq.heappush(heap,-i)
        while len(heap)>=2:
            a=-heapq.heappop(heap)
            b=-heapq.heappop(heap)
            a-=1
            b-=1
            if(a>0):
                heapq.heappush(heap,-a)
            if(b>0):
                heapq,heappush(heap,-b)
            time+=1
        if heap:
            return time+(-heap[0])
        return time


            
        