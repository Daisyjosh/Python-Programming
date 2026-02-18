class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def preorderTraversal(root):
    preorder = []
    if root is None:
        return preorder
    st = []
    st.append(root)
    while st:
        root = st.pop()
        preorder.append(root.data)
        if(root.right):
            st.append(root.right)
        if(root.left):
            st.append(root.left)
    return preorder
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(preorderTraversal(root))
