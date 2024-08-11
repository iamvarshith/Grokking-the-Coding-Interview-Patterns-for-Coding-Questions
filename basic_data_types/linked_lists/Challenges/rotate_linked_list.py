from basic_data_types.linked_lists.single_linked_lists import LinkedList


def rotateRight( head, k ):
    if head is None:
        return head

    slow_pointer = fast_pointer = head
    length = length_of_ll(head)
    nonrepetative_rotation = k % length


    if nonrepetative_rotation == 0:
        return head

    for _ in range(nonrepetative_rotation):
        fast_pointer = fast_pointer.next

    while fast_pointer.next:
        fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next

    fast_pointer.next = head
    head = slow_pointer.next
    slow_pointer.next = None
    return head



def length_of_ll( head):
    if head is None:
        return 0
    length = 1
    while head.next:
        head = head.next
        length += 1
    return length


if __name__ == "__main__":
    list1 = LinkedList()
    for i in range(1,9):
        list1.insert_at_tail(i)
    new_head = rotateRight(list1.head,35)
    while new_head:
        print(new_head.data)
        new_head = new_head.next
