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

    def remove(self,data):
        if not self.root:
            print("Tree is empty")
            return
        if self.root.data == data:
            self.root = None
            return
        ParentNode = self.findParentNode(data,self.root)


    def findParentNode(self,data,node=None):
        for child in node.children:
            if child.data == data:
                return node
            nodefound = self.findParentNode(data,child)
            if nodefound:
                return nodefound

        return None



    def display(self,depth = 0,node = None):
        if not node:
            node = self.root

        print(" "*depth,self.root.data)
        for child in node.children:
            self.display(depth+1,child)




treenode = Tree()
treenode.add(1)
treenode.add(2,1)
treenode.add(3,1)
treenode.add('a',1)
treenode.add(4,2)
treenode.add(5,2)
treenode.add(6,3)
treenode.add(7,3)

treenode.display(node=treenode.root)
