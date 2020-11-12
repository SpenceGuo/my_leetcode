# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        temp = []
        p1 = head
        while p1 != None:
            temp.append(p1.val)
            p1 = p1.next

            p2 = ListNode(temp[-1])
            result = p2
        for i in range(len(temp) - 2, -1, -1):
            p2.next = ListNode(temp[i])
            p2 = p2.next
        return result
