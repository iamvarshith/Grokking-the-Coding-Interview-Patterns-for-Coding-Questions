class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root=None, key=None):
    if root.data is None:
        root = Node(key)

    elif root.data < key:
        if root.right is None:
            root.right = Node(key)
        if root.right:
            return insert(root=root.right, key=key)
    elif root.data > key:
        if root.left is None:
            root.left = Node(key)
        if root.left:
            return insert(root=root.left, key=key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data,end = " ")
        preorder(root.left)
        preorder(root.right)
if __name__ == "__main__":
    r = Node(20)
    insert(r, 8)
    insert(r, 22)
    insert(r, 24)
    insert(r, 4)
    insert(r, 12)
    insert(r, 10)
    insert(r, 14)
    print("inorder")
    inorder(r)
    print("preorder")
    preorder(r)
