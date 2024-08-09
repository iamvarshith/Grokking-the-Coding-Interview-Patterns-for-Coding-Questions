"""Challenge: Remove Duplicates from a Linked List

Statement
Given the head of a singly linked list, remove any duplicate nodes from the list in place, ensuring that only one occurrence of each value is retained in the modified list.

"""

from basic_data_types.linked_lists.single_linked_lists import LinkedList


def remove_duplicates(head):
    outernode = head
    innernode = None
    while outernode:
        innernode = outernode
        while innernode:
            if innernode.next:
                if outernode.data == innernode.next.data:
                    innernode.next = innernode.next.next
                else:
                    innernode = innernode.next
            else:
                innernode = innernode.next
        outernode = outernode.next
    return head


if __name__ == "__main__":
    new_list = LinkedList()
    new_list.insert_at_tail('40')
    new_list.insert_at_tail('60')
    new_list.insert_at_tail('30')
    new_list.insert_at_tail('30')
    new_list.insert_at_tail('30')
    new_list.insert_at_tail('30')
    new_list.insert_at_tail('40')
    new_list.insert_at_tail('40')
    new_list.insert_at_head('690')
    remove_duplicates(new_list.head)
    new_list.print_linkedlist()
