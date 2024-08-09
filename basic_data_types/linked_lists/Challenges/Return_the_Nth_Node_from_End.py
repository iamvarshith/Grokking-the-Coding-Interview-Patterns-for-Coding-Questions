"""
Challenge: Return the Nth Node from End

Statement
Given the head of a linked list, return the nth node from the end of the linked list.

"""

from basic_data_types.linked_lists.single_linked_lists import LinkedList

def find_nth_element(head, n):
    if head is None or n <= 0:
        print("Invalid input")
        return

    fastpointer = head
    slowpointer = head

    # Move fastpointer n nodes ahead
    for _ in range(n):
        if fastpointer is None:
            print("n is larger than the length of the list")
            return
        fastpointer = fastpointer.next

    # Move both pointers until fastpointer reaches the end
    while fastpointer:
        fastpointer = fastpointer.next
        slowpointer = slowpointer.next

    # Slowpointer is now at the nth node from the end
    if slowpointer:
        print(slowpointer.data)
    else:
        print("The list is shorter than n")


if __name__ == "__main__":
    list1 = LinkedList()
    for i in [-1,-2,3,4,5,-6,7,8,9] :
        list1.insert_at_tail(i)
    list1.print_linkedlist()

    find_nth_element(list1.head, 1)
