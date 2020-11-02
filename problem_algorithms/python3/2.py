# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        # 头节点，一般默认为空; 其中p为指针
        sum_Node = p = ListNode(None)
        while((l1 != None) or (l2 != None)) or carry:
            # 此处代码写法和简洁
            # l1.val if l1 else 0 ：这样可以保证在两个链表长度不一样时将短的链表没有的值用0代替
            p.next = ListNode(((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry) % 10)
            if ((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry) > 9:
                carry = 1
            else:
                carry = 0
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return sum_Node.next


# testing part
# l1 = ListNode(9)
# l1.next = ListNode(9)
# l1.next.next = ListNode(9)
# l1.next.next.next = ListNode(9)
# l1.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next = ListNode(9)
# l1.next.next.next.next.next.next = ListNode(9)
#
# l2 = ListNode(9)
# l2.next = ListNode(9)
# l2.next.next = ListNode(9)
# l2.next.next.next = ListNode(9)
#
# x = Solution()
# result = x.addTwoNumbers(l1, l2)
# while(result != None):
#     print(result.val)
#     result = result.next
