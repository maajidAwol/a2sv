# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        temp = head
        count = 0
        ans =[] *k
        while temp:
            count+=1
            temp = temp.next
        each = count//k
        extra = count%k
        nav = head
        for i in range(k):
            t = ListNode()
            h= t
            if  nav:
                for i in range(each):
                    if nav:
                        t.next = ListNode(nav.val)
                        t = t.next
                        nav = nav.next
                if extra and nav:
                    t.next = ListNode(nav.val)
                    t = t.next
                    nav = nav.next
                    extra -=1
            ans.append(h.next)
        return ans