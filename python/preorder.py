class Treenode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def preorder_traversal(node):
        if node is not None:
            print(node.key,end=" ")
            Treenode.preorder_traversal(node.left)
            Treenode.preorder_traversal(node.right)
root=Treenode(10) 
root.left=Treenode(5)
root.right=Treenode(15)
print("preorder traversal")
Treenode.preorder_traversal(root)          