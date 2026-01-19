class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
class CDll:
    def __init__(self):
        self.head = None
    
    def fw_traversal(self):
        a = self.head
        while True:
            print(a.data,end=" ")
            a = a.next
            if a == self.head:
                break
    def delete_at_SpecificNode(self,position):
        print()
        a = self.head
        for i in range(1,position-1):
            a = a.next
            if a is self.head:
                print("Position out of range")
                return
        target = a.next
        if target == self.head:
            print("Position out of range")
            return

        a.next = target.next
        target.next.prev = a
    
        
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

        
# next..
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# prev...
n2.prev = n1
n3.prev = n2
n4.prev = n3
n5.prev = n4

# circular..
n1.prev = n5  
n5.next = n1

cdll = CDll()
cdll.head = n1

cdll.fw_traversal()
cdll.delete_at_SpecificNode(3)
cdll.fw_traversal()



