import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq=Counter(tasks)
        heap=[]
        for count in freq.values():
            heapq.heappush(heap,-count)
        q=deque()
        time=0
        while heap or q:
            time+=1
            if heap:
                count=-heapq.heappop(heap)
                count-=1
                if count>0:
                    q.append((-count,time+n))
            if q and q[0][1]==time:
                count,available_time=q.popleft()
                heapq.heappush(heap,count)
        return time
