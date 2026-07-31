class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_values=sorted(set(arr))
        rank={}
        for i,value in enumerate(sorted_values):
            rank[value]=i+1
        ans=[]
        for value in arr:
            ans.append(rank[value])
        return ans