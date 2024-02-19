# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode()
        great = ListNode()
        ret = less
        great_head = great
        while head:
            temp = ListNode(head.val)
            if head.val < x:
                less.next = temp
                less = less.next
            else:
                great.next = temp
                great = great.next
            head = head.next
        less.next = great_head.next
        return ret.next