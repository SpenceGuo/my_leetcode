# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 双指针解法，方便快捷
        p1 = p2 = head
        for i in range(0, k - 1):
            p2 = p2.next
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        return p1
