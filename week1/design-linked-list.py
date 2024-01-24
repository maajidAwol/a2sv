class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
    def get(self, index: int) -> int:
        current = self.dummy.next
        p = current
        i = 0
        while p:
           
            print(p.val)
            p = p.next
        while current:
            if i == index:

                return current.val
            current = current.next
            i+=1
        
        return -1

    def addAtHead(self, val: int) -> None:
        var = Node(val)
        var.next = self.dummy.next
        self.dummy.next  = var
       

    def addAtTail(self, val: int) -> None:
        curr = self.dummy
        while curr.next:
            curr = curr.next
        new = Node(val)
        curr.next = new

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.dummy
        new = Node(val)
        i = 0
        while curr:
            if index ==i:
                new.next = curr.next
                curr.next = new
            curr = curr.next
            i+=1
        pass

    def deleteAtIndex(self, index: int) -> None:
        i =0
        curr = self.dummy
        while curr and curr.next:
            if i == index:
                curr.next = curr.next.next
            curr = curr.next
            i+=1
        pass

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)