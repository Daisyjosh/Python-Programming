class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
class CDll:
    def __init__(self):
        self.head = None
    


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


