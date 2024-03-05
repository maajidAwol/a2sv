# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = None
        r = None
        nav = ListNode()
        nav.next = head
        head = nav
        i =0
        while nav:
            if i ==left-1:
                l = nav
            elif i ==right:
                r = nav
            i+=1
            nav = nav.next
        
        mid = mid1 = l.next
        l.next = None
        end = r.next
        r.next = None
        l.next = self.reverse(mid)
        mid1.next = end
        return head.next
    def reverse(self,head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev     