# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = head
        nav = head
        count = 0
        while nav:
            count +=1
            nav = nav.next
        mid = count //2
        prev = None
        while mid:
            mid -=1
            nxt = rev.next
            rev.next = prev
            prev = rev
            rev = nxt
        if count%2:
            rev= rev.next
        while rev:
            if rev.val != prev.val:
                return False
            rev =rev.next
            prev = prev.next
        return True            