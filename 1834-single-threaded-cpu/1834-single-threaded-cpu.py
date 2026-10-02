import heapq
class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        sorted_tasks=[]
        for i in range(len(tasks)):
            enqueue_time,processing_time=tasks[i]
            sorted_tasks.append((enqueue_time,processing_time,i))
        sorted_tasks.sort()
        heap=[]
        ans=[]
        time=0
        i=0
        n=len(tasks)
        while i<n or heap:
            if not heap and sorted_tasks[i][0]>time:
                time=sorted_tasks[i][0]
            while i<n and sorted_tasks[i][0]<=time:
                enqueue,processing_time,index=sorted_tasks[i]
                heapq.heappush(heap,(processing_time,index))
                i+=1
            processing,index=heapq.heappop(heap)
            ans.append(index)
            time+=processing
        return ans

