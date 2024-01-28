# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        curr = head
        prev = None
        while curr:
           nxt = curr.next
           curr.next = prev
           prev = curr
           curr = nxt
        i =0
        count=0
        while prev:
            count = count + (prev.val *(2**i))
            i+=1
            prev = prev.next
        return count