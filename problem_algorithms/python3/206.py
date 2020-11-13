# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p = head
        data = []
        while p:
            data.append(p.val)
            p = p.next
        p1 = result = ListNode(0)
        for j in range(len(data)-1, -1, -1):
            p1.next = ListNode(data[j])
            p1 = p1.next
        return result.next