# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:

        lenA = 0
        currA = headA

        while currA:
            lenA += 1
            currA = currA.next
        currB = headB
        lenB = 0
        while currB:
            lenB += 1
            currB = currB.next
        a = headA
        b = headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                a = a.next
        else:
            for _ in range(lenB - lenA):
                b = b.next
        while a != b:
            a = a.next
            b = b.next
        return a
