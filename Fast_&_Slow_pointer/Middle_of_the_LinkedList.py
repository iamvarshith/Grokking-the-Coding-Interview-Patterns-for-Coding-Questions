"""
Problem Statement#

Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.

If the total number of nodes in the LinkedList is even, return the second middle node.

Example 1:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
Output: 3

Example 2:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
Output: 4

Example 3:

Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
Output: 4

"""
from basic_data_types.linked_list import Linkedlist


def middle_linked_list(linked_list):
    x1_pointer = linked_list.head
    x2_pointer = linked_list.head

    while x2_pointer is not None and x2_pointer.next is not None:

        x1_pointer = x1_pointer.next
        x2_pointer = x2_pointer.next.next

    return x1_pointer


linked_list = Linkedlist()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)
linked_list.insert(5)
linked_list.insert(6)
linked_list.insert(7)
linked_list.insert(8)
linked_list.insert(9)



print(middle_linked_list(linked_list).data)