# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([root])
        ans=[]
        curr_level=1
        while q:
            level_size=len(q)
            level=[]
            for _ in range(level_size):
                node=q.popleft()
                level.append(node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            if((curr_level)%2!=0):
                ans.append(level)
            else:
                ans.append(level[::-1])
            curr_level+=1
        return ans






        