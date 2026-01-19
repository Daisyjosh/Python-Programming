class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
class CDll:
    def __init__(self):
        self.head = None
    
    def bw_traversal(self):
        a = self.head.prev
        while True:
            print(a.data,end=" ")
            a = a.prev
            if a == self.head.prev:
                break

    


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

cdll.bw_traversal()



