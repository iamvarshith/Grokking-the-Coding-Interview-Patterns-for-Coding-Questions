class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.indicator = None

    def insert(self, key=None):

        if self.data is None:
            self.__init__(key)

        elif self.data < key:
            if self.right is None:
                self.right = Node(key)
            if self.right:
                return Node.insert(self=self.right, key=key)
        elif self.data > key:
            if self.left is None:
                self.left = Node(key)
            if self.left:
                return Node.insert(self=self.left, key=key)

    def inorder(self):
        if self is not None:
            Node.inorder(self.left)
            print(self.data)
            Node.inorder(self.right)


r = Node(20)
Node.insert(self=r, key=8)
Node.insert(r, 22)
Node.insert(r, 24)
Node.insert(r, 4)
Node.insert(r, 12)
Node.insert(r, 10)
Node.insert(r, 14)

Node.inorder(r)
