# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 我们使用两个指针 node1，node2 分别指向两个链表 headA，headB 的头结点，
        # 然后同时分别逐结点遍历，当 node1 到达链表 headA 的末尾时，重新定位到链表 headB 的头结点；
        # 当 node2 到达链表 headB 的末尾时，重新定位到链表 headA 的头结点。
        # 这样，当它们相遇时，所指向的结点就是第一个公共结点
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
