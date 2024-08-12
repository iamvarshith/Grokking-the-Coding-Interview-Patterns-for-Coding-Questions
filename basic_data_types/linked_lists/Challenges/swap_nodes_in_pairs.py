from basic_data_types.linked_lists.single_linked_lists import LinkedList


def swapPairs(head):
    odd_node = head if head is not None else None
    even_node = head.next if head.next is not None else None
    if odd_node & even_node is None:
        return head
    if even_node is None:
        return head

    while odd_node & even_node:
        next_odd_node = odd_node.next.next if odd_node.next.next is not None else None
        next_even_node = even_node.next.next if even_node.next.next is not None else None
        odd_node.next = odd_node
        even_node.next = even_node


