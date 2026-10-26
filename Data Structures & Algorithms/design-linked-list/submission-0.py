class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        current = self.head
        position = 0
        if index< 0 or index >=self.size:
            return -1

        while position < index:
            current = current.next
            position +=1

        return current.val

    def addAtHead(self, val: int) -> None:
        
        newNode = ListNode(val)

        newNode.next = self.head
        self.head = newNode
        self.size+=1

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            self.size  +=1
            return
        current = self.head
        while current.next:
            current = current.next
        
        current.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        if index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return
        
        newNode = ListNode(val)
        current = self.head
        for i in range(index-1):
            current = current.next
        newNode.next = current.next
        current.next = newNode
        self.size +=1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        
        current = self.head
        for i in range(index-1):
            current = current.next
        current.next = current.next.next
        self.size -=1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)