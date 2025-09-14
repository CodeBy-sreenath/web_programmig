class UserNode:
    def __init__(self,name,username,email):
        self.name=name
        self.username=username
        self.email=email
        self.left=None
        self.right=None
class UserDb:
    def __init__(self):
        self.root=None
    def insert(self,name,username,email):
        self.root=self._insert(self.root,name,username,email)
    
    def _insert(self,node,name,username,email):
        if node is None:
            return UserNode(name,username,email)
        if name<node.name:
            node.left=self._insert(node.left,name,username,email)
        elif name>node.name:
            node.right=self._insert(node.right,name,username,email)
        else:
            raise ValueError("Duplicate user name is not allowed")
        return node
    def search(self,name):
        return self._search(self.root,name)
    def _search(self,node,name):
        if node is None or node.name==name:
            return node
        if name<node.name:
            return self._search(node.left,name)
        return self._search(node.right,name)
                    
    def inorder(self):
        users=[]
        self._inorder(self.root,users)
        return users
    def _inorder(self,node,users):
        if node:
            self._inorder(node.left,users)
            users.append((node.name,node.username,node.email))
            self._inorder(node.right,users)
if __name__=="__main__":
    db=UserDb()
    db.insert("Alice","alice123","alice@gmail.com")
    db.insert("Charlie", "charlie_boy", "charlie@example.com")
    db.insert("Bob", "bobby", "bob@example.com")
    db.insert("David", "david_01", "david@example.com")
    print("user sorted by inorder traversal")
    for user in db.inorder():
        print(user)
    name_to_search = "Charlie"
    result = db.search(name_to_search)
    if result:
        print(f"\nFound: {result.name}, {result.username}, {result.email}")
    else:
        print(f"\nUser '{name_to_search}' not found")    
               