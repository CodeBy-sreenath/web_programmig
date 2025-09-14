class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,key,root):
        if root is None:
            return Node(key)
        if key<root.key:
            root.left=self.insert(key,root.left)
        elif key>root.key:
            root.right=self.insert(key,root.right)
        return root
    def search(self,key,root):
        if root is None or root.key==key:
            return root
        if key<root.key:
            return self.search(key,root.left)
        return self.search(key,root.right) 
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key,end=" ")
            self.inorder(root.right)
    def find_min(self,root):
        current=root
        while current.left is not None:
            current=current.left 
        return current              
    def find_max(self,root):
        current=root
        while current.right is not None:
            current=current.right
        return current            
if __name__=="__main__":
    tree=BST()
    root=None
    nums=[20,10,30,2,15,25,35]
    for num in nums:
        root=tree.insert(num,root)
    print("Inorder traversal:")
    tree.inorder(root)

    print("\n\nSearch for 40:", "Found" if tree.search(40, root) else "Not Found")

    print("Minimum value:", tree.find_min(root).key)
    print("Maximum value:", tree.find_max(root).key)    
            