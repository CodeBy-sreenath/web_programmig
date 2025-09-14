class Treenode:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def parse_tuple(data):
        if isinstance(data, tuple) and len(data) == 3:
            node = Treenode(data[1])
            node.left = Treenode.parse_tuple(data[0])
            node.right = Treenode.parse_tuple(data[2])
        elif data is None:
            node = None
        else:
            node = Treenode(data)
        return node


# -------------------------
# Example usage OUTSIDE class
# -------------------------
node0 = Treenode(10)
node1 = Treenode(5)
node2 = Treenode(15)

tree = node0
tree.left = node1
tree.right = node2

print(tree.key)   # 10
print(node0.key)  # 10
print(node1.key)  # 5
print(node2.key)  # 15

# Example using parse_tuple
tree2 = Treenode.parse_tuple(((1, 2, None), 3, (None, 4, 5)))
print(tree2.key)          # 3 (root)
print(tree2.left.key)     # 2
print(tree2.right.key)    # 4
