from trees.binary_tree import Node, insert, inorder, preorder

root_list = []


def sum_length(root: Node, root_list: list, key: int):

    # if root.data is None:
    #     return None

    if root.data:
        root_list.append(root.data)
        if sum(root_list) == key:
            print(sum(root_list))
            print(root_list)

    if root.left is not None:
        sum_length(root.left, root_list, key)
    if root.right is not None:
        sum_length(root.right, root_list, key)
    # if root.left is None and root.right is None:
    #     root_list.remove(root.data)
    root_list.remove(root.data)

if __name__ == "__main__":
    r = Node(20)
    insert(r, 8)
    insert(r, 22)
    insert(r, 24)
    insert(r, 4)
    insert(r, 12)
    insert(r, 10)
    insert(r, 14)
    sum_length(r, root_list, 66)
    # print("inorder")
    # inorder(r)
    # print("preorder")
    # preorder(r)