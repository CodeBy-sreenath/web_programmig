class Treenode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def postorder_traversal(node):
        if node is not None:
            Treenode.postorder_traversal(node.left)
            Treenode.postorder_traversal(node.right)
            print(node.key,end=" ")
root=Treenode(10)
root.left=Treenode(5)
root.right=Treenode(15)
Treenode.postorder_traversal(root)    
#for finding the height of the tree
def tree_height(node):
    if node is None:
        return -1
    return 1 + max(tree_height(node.left),tree_height(node.right))

# for finding the number of nodes
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left)+tree_size(node.right)
        
            