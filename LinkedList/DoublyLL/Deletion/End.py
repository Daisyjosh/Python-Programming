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
    def delete_at_end(self):
        a = self.head.next
        before = self.head
        while a.next is not None:
            a = a.next
            before = before.next
        before.next = None
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
dll.delete_at_end()
dll.fr_traversal()

