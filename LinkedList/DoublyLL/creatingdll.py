class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
        self.head = None
        print("Daisy")
dll = Dll()
n1 = Node(5)
dll.head = n1

