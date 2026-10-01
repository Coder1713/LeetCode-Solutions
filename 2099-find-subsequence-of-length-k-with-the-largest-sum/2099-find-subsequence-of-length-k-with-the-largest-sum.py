import heapq
class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,(nums[i],i))
        while len(heap)>k:
            heapq.heappop(heap)
        heap.sort(key=lambda x: x[1])
        return [x for x,num in heap]
       