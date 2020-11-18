# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        p = head
        num_list = []
        while p:
            num_list.append(str(p.val))
            p = p.next
        str_1 = ''.join(num_list)
        return int(str_1, 2)


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
x = Solution()
print(x.getDecimalValue(head))