from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        heap=[]
        for key in freq:
            heapq.heappush(heap,(-freq[key],key))
        ans=""
        while heap:
            count,ch=heapq.heappop(heap)
            ans+=ch*(-count)
        return ans


