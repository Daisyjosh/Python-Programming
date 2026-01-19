#Insertion at the beginning 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        if self.head is None:
            print("Singly Linked List is Empty")
        else:
            a = self.head
            while a is not None:
                print(a.data,end=" ")
                a = a.next

    def delete_at_specificNode(self,position):
        print()
        prev = self.head
        a = self.head.next
        for i in range(1,position-1):
            a = a.next
            prev = prev.next
        prev.next = a.next
        a.next = None
        

n1 = Node(5)
sll = Sll()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
n4 = Node(20)
n3.next = n4
n5 = Node(25)
n4.next = n5
sll.traversal()
sll.delete_at_specificNode(3)
sll.traversal()


