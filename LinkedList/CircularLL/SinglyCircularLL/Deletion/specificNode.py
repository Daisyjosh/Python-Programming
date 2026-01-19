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
    def delete_at_specificNode(self,position):
        print()
        # empty list
        if self.head is None:
            print("List is empty")
            return

        # if only one node
        if position == 1:
            if self.head.next == self.head:
                self.head = None
                return
        
            # if more than one node
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            return 

        # if position > 1

        prev = self.head
        curr = self.head.next
        count = 2

        while curr != self.head:
            if count == position:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            count += 1
        print("Position out of range")
        

        
        

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
scll.delete_at_specificNode(3)
scll.traversal()

