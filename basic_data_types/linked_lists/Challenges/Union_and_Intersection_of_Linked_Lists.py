from basic_data_types.linked_lists.single_linked_lists import LinkedList

"""
Given the heads of two linked lists, head1 and head2, as inputs. Implement the union and intersection functions for the linked lists. The order of elements in the output lists doesn’t matter.

Here’s how you will implement the functions:

Union: This function will take two linked lists as input and return a new linked list containing all the unique elements.

Intersection: This function will take two linked lists as input and return all the common elements between them as a new linked list.


"""


def union(head1, head2):
    # Will join head1 and head2 to create one list and remove duplicates from that.
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    current = head1
    while current.next:
        current = current.next
    current.next = head2

    remove_duplicate(head1)

    return head1


def remove_duplicate(head):
    if not head:
        return head

    slow_pointer = head

    while slow_pointer:
        fast_pointer = slow_pointer
        while fast_pointer.next:
            if fast_pointer.next.data == slow_pointer.data:
                fast_pointer.next = fast_pointer.next.next
            else:
                fast_pointer = fast_pointer.next
        slow_pointer = slow_pointer.next
    return head

def intersection(head1, head2):

    return head1


if __name__ == "__main__":
    list1 = LinkedList()
    for i in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]:
        list1.insert_at_tail(i)
    list1.print_linkedlist()
    list2 = LinkedList()
    for i in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]:
        list2.insert_at_tail(i)
    list2.print_linkedlist()

    union(list1.head,list2.head)