# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nav = head
        odd = ListNode()
        rt = odd
        even = ListNode()
        ev = even
        i = 0
        while nav:
            if i%2:
                even.next = ListNode(nav.val)
                even = even.next
            else:
                odd.next = ListNode(nav.val)
                odd = odd.next
            i +=1
            nav = nav.next
        odd.next = ev.next
        return rt.next
            
        
        