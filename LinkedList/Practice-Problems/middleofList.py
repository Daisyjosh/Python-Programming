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

    def middleElement(self,head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
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

# Middle Element
middle_element = sll.middleElement(sll.head)

print(middle_element)