from collections import deque
class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

def BreadthFirstSearch(root):
    if root is None:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(result)
    


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
BreadthFirstSearch(root)
