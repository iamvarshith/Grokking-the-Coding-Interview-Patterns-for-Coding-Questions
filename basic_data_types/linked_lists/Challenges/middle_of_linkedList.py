from basic_data_types.linked_lists.single_linked_lists import LinkedList

"""Statement
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node. 
This happens when the length of the list is even 1/2(length) + 1,  
and the second middle node occurs at Otherwise, if the length of the list is odd, 
the middle node occurs at 1/2(length) th position 
"""


def find_middle_element(head):
    if head and head.head.next:
        x1pointer = head.head
        x2pointer = head.head.next
        while x2pointer:
            if x2pointer.next is None:
                x1pointer = x1pointer.next
                break
            if x1pointer.next.next:
                x2pointer = x2pointer.next.next
                x1pointer = x1pointer.next

        print(x1pointer.data)
    else:
        return head


if __name__ == "__main__":
    new_list = LinkedList()
    new_list.insert_at_tail('1')
    new_list.insert_at_tail('2')
    new_list.insert_at_tail('3')
    new_list.insert_at_tail('4')
    new_list.insert_at_tail('5')
    new_list.insert_at_tail('6')
    new_list.print_linkedlist()
    find_middle_element(new_list)
