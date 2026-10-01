from collections import Counter
import heapq
class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        freq=Counter(arr)
        n=len(arr)
        heap=[]
        ans_set=set()
        rem_len=n
        for key in freq:
            heapq.heappush(heap,(-freq[key],key))
        while rem_len>(n/2):
            count,num=heapq.heappop(heap)
            rem_len-=(-count)
            ans_set.add(num)
            
        return len(ans_set)

        