import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap=[]
        for i in range(len(arr)):
            heapq.heappush(heap,(-abs(arr[i]-x),-arr[i]))
        while len(heap)>k:
            heapq.heappop(heap)
        ans=[-x for diff,x in heap]
        answer=sorted(ans)
        return answer

