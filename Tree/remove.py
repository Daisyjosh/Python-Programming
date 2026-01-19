class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
    
class Tree:
    def __init__(self):
        self.root = None

    def add(self,data,parentdata=None):
        node = TreeNode(data)
    
        if self.root is None:
            self.root = node
            return 
        ParentNode = self.findNode(parentdata,self.root)

        if not ParentNode:
            print("ParentNode not found")
            return
        ParentNode.children.append(node)

    def findNode(self,data,node):
        if node.data == data:
            return node
        for child in node.children:
            nodeFound = self.findNode(data,child)
            if nodeFound:
                return nodeFound
        return None
            





treenode = Tree()
treenode.add(1)
treenode.add(2,1)
treenode.add(3,1)
treenode.add(4,3)
