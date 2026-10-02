import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        heap=[]
        count=0
        for num in nums:
            heapq.heappush(heap,num)
        while (len(heap)>=2):
            if heap[0]<k: 
                count+=1
            a=heapq.heappop(heap)
            b=heapq.heappop(heap)
            new_num=(min(a,b)*2)+max(a,b)
            
            heapq.heappush(heap,new_num)
            
        return count


 