class Treenode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder_traversal(node):
    """Perform inorder traversal and print the keys."""
    if node is not None:
        inorder_traversal(node.left)   # 1. Visit left subtree
        print(node.key, end=" ")       # 2. Visit root
        inorder_traversal(node.right)  # 3. Visit right subtree


# --------------------
# Example usage
# --------------------
# Create tree:
#        10
#       /  \
#      5    15
#
root = Treenode(10)
root.left = Treenode(5)
root.right = Treenode(15)

print("Inorder Traversal:")
inorder_traversal(root)
