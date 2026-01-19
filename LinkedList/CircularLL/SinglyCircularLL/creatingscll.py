class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SCll:
    def __init__(self):
        self.head = None

n1 = Node(5)
n2 = Node(6)
n3 = Node(7)
n4 = Node(8)
n5 = Node(9)

n1.next = n2
n2.next = n1

scll = SCll()
scll.head = n1
