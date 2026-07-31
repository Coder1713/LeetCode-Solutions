class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        freq=Counter(hand)
        heap=list(freq.keys())
        heapq.heapify(heap)
        while heap:
            while heap and freq[heap[0]]==0:
                heapq.heappop(heap)
            if not heap:
                break
            start=heap[0]
            for card in range(start,start+groupSize):
                if freq[card]==0:
                    return False
                freq[card]-=1
        return True
