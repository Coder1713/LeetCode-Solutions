import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap=[]
        x=multiplier
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))
        for _ in range(k):
            num,index=heapq.heappop(heap)
            new_num=num*x
            heapq.heappush(heap,(new_num,index))
        heap.sort(key=lambda x:x[1])
        return [num for num,index in heap]
