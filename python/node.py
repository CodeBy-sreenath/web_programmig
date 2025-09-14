class Node:
    def __init__(self,root):
        
        pass
    def lca(root, n1, n2):
        
        if root is None:
            return None
        if n1 < root.key and n2 < root.key:
            return lca(root.left, n1, n2)
        if n1 > root.key and n2 > root.key:
            return lca(root.right, n1, n2)
        return root

    print("LCA of 5 and 15:", lca(root, 5, 15).key)  # 10
    print("LCA of 25 and 35:", lca(root, 25, 35).key)  # 30
