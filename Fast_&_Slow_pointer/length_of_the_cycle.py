from basic_data_types.linked_list import Linkedlist
"""
Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.

Solution: We can use the LinkedList_cycle solution to find the cycle in the LinkedList. Once the fast and slow pointers meet, 
we can save the slow pointer and iterate the whole cycle with another pointer until we see the slow pointer again to 
find the length of the cycle.
"""

def detect_cycle_item(linked_list):
    fast_pointer = linked_list.head
    slow_pointer = linked_list.head

    while fast_pointer and fast_pointer.next is not None:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        if slow_pointer == fast_pointer:
            return length_linked_list(slow_pointer)
    return "No cycle in this"


def length_linked_list(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


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
    print(detect_cycle_item(linked_list))
