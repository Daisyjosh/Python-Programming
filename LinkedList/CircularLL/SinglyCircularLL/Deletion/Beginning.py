class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SCll:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head is None:
            print("Circular Singly Linked List is Empty")
            return
        a = self.head
        while True:
            print(a.data,end=" ")
            a = a.next
            if a == self.head:
                break
    def delete_at_beginning(self):
        print()
        # empty list
        if self.head is None:
            print("List is empty")
            return

        # if only one node
        if self.head.next == self.head:
            self.head = None
            return
        
        # if more than one node
        a = self.head
        while a.next != self.head:
            a = a.next
        self.head = self.head.next
        a.next = self.head

        
        

n1 = Node(5)
n2 = Node(6)
n3 = Node(7)
n4 = Node(8)
n5 = Node(9)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n1

scll = SCll()
scll.head = n1

scll.traversal()
scll.delete_at_beginning()
scll.traversal()

