import heapq
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        n=len(score)
        rank=[0]*n
        heap=[]
        for x in score:
            heapq.heappush(heap,-x)
        rank={}
        for i in range(n):
            rank[-heapq.heappop(heap)]=i+1
        ans=[]
        for i in range(n):

            if(rank[score[i]]==1):
                ans.append("Gold Medal")
            elif(rank[score[i]]==2):
                ans.append("Silver Medal")
            elif(rank[score[i]]==3):
                ans.append("Bronze Medal")
            else:
                ans.append(str(rank[score[i]]))
        return ans

