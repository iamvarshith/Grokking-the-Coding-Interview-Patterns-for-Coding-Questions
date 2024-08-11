""""
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

"""

"""
If we know the length of the LinkedList cycle, we can find the start of the cycle through the following steps:

    * Take two pointers. Let’s call them pointer1 and pointer2.
    * Initialize both pointers to point to the start of the LinkedList.
    * We can find the length of the LinkedList cycle using the approach discussed in LinkedList Cycle. Let’s assume that the length of the cycle is ‘K’ nodes.
    * Move pointer2 ahead by ‘K’ nodes.
    * Now, keep incrementing pointer1 and pointer2 until they both meet.
    * As pointer2 is ‘K’ nodes ahead of pointer1, which means, pointer2 must have completed one loop in the cycle when both pointers meet. Their meeting point will be the start of the cycle.

"""

from basic_data_types.linked_lists.linked_list import Linkedlist
from length_of_the_cycle import detect_cycle_item


def length_of_linked_list(element_in_cycle):
    length_cycle = 0
    pointer = element_in_cycle
    while True:
        pointer = pointer.next
        length_cycle += 1
        if pointer == element_in_cycle:
            break
    return length_cycle


def detect_head(linked_list):
    """

    :param linked_list:
    :return: Start of LinkedList Cycle( head )
    """
    # * Take two pointers. Let’s call them slow_pointer and fast_pointer.
    #  * Initialize both pointers to point to the start of the LinkedList.

    slow_pointer = l.head
    fast_pointer = l.head

    # Finding the element in the ll to find the length.
    element_in_cycle = detect_cycle_item(l)

    #     We can find the length of the LinkedList cycle using the approach discussed in LinkedList Cycle.
    #     Let’s assume that the length of the cycle is ‘length_cycle’ nodes.

    length_cycle = length_of_linked_list(element_in_cycle)

    # Move fast_pointer ahead by ‘length_cycle’ nodes.
    for i in range(length_cycle):
        fast_pointer = fast_pointer.next

    # Now, keep incrementing slow_pointer and fast_pointer until they both meet.

    while True:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

        # As fast_pointer is ‘length_cycle’ nodes ahead of slow_pointer, which means, fast_pointer must have
        # completed one loop in the cycle when both pointers meet. Their meeting point will be the start of the cycle.

        if slow_pointer == fast_pointer:
            print(slow_pointer.data, fast_pointer.data)
            return slow_pointer


if __name__ == '__main__':
    l = Linkedlist()
    for i in range(50):
        l.insert(i)
    l.circular_linked_list(19)
    detect_head(l)
