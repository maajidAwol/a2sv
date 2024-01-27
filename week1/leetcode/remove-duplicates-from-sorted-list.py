# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        elements = set()
        new = ListNode()
        rt = new
        while head:
            if head.val not in elements:
                elements.add(head.val)
                temp = ListNode(head.val)     
                new.next = temp
                new = new.next
            head = head.next
        return rt.next