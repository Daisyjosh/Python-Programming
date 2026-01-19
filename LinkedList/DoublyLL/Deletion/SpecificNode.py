# Forward Traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
        self.head = None
        print("Daisy")

    def fr_traversal(self):
        if self.head is None:
            print("Doubly Linked list is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a = a.next
    def deletion_at_specificNode(self,position):
        print()
        a = self.head.next
        before = self.head
        for i in range(1,position-1):
            a = a.next
            before = before.next
        before.next = a.next
        a.next.prev = before
        a.next = None
        a.prev = None
        
        
dll = Dll()
n1 = Node(5)
dll.head = n1
n2 = Node(10)
n1.next = n2
n2.prev = n1
n3 = Node(15)
n2.next = n3
n3.prev = n2
n4 = Node(20)
n3.next = n4
n4.prev = n3
dll.fr_traversal()
dll.deletion_at_specificNode(3)
dll.fr_traversal()

