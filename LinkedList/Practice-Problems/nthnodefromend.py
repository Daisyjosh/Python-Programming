# nth node from end of linked list

class Node:
    def __init__(self, data):
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
            while a:
                print(a.data, end=" ")
                a = a.next
        print()

    def NthNodeFromEnd(self,head,n):
        fast = slow = head

        for i in range(n):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.data


# Creating nodes
n1 = Node(5)
n2 = Node(10)
n3 = Node(15)
n4 = Node(20)
n5 = Node(25)

# Linking nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Creating list
sll = Sll()
sll.head = n1

# Original list
print("Original list:")
sll.traversal()

# Nth Node From End of the LL
Nth_node = sll.NthNodeFromEnd(sll.head,3)
print(Nth_node)

