from basic_data_types.linked_list import Linkedlist


def has_a_cycle(linked_list):
    fast_pointer = linked_list.head
    slow_pointer = linked_list.head

    while fast_pointer and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        if slow_pointer == fast_pointer:
            return True

    return False


linked_list = Linkedlist()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)
linked_list.insert(6)
linked_list.insert(7)
linked_list.circular_linked_list(1)

if __name__ == "__main__":
    print(has_a_cycle(linked_list))
