# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        nodeSet = set()
        while head:
            if head in nodeSet:
                return head
            nodeSet.add(head)
            head = head.next
        return None


class Solution_1:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow, fast = head, head
        while slow != fast:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
        if fast == slow:
            ptr = head
            while slow != ptr:
                slow = slow.next
                ptr = ptr.next
            return slow
        return None


nodeList = ListNode(3)
nodeList.next = ListNode(2)
nodeList.next.next = ListNode(0)
nodeList.next.next.next = ListNode(-4)
nodeList.next.next.next.next = nodeList.next
x = Solution_1()
print(x.detectCycle(nodeList))

