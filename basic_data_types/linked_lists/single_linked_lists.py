# Basic Linked List Operations

# The primary operations which are generally a part of the LinkedList class are listed below:
#
# get_head() - returns the head of the list
# insert_at_tail(data) - inserts an element at the end of the linked list
# insert_at_head(data) - inserts an element at the start/head of the linked list
# delete(data) - deletes an element with your specified value from the linked list
# delete_at_head() - deletes the first element of the list
# search(data) - searches for an element with the specified value in the linked list

# is_empty() - returns true if the linked list is empty

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head:
            current_head = self.head
            while current_head.next:
                current_head = current_head.next
            current_head.next = new_node
        else:
            self.head = new_node

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def print_linkedlist(self):
        current = self.head
        while current:
            print(current.data, current.next)
            current = current.next

    def search_element(self, value):
        if self.head:
            node_element = self.head
            while node_element:
                if node_element.data == value:
                    print("Yes")
                    return True
                else:
                    node_element = node_element.next
            print("NO")
            return False

    def delete_node_by_value(self, value):

        deleted = False

        if self.head.data == value:
            self.head = self.head.next
            deleted = True
            return deleted

        current = self.head
        previous = None

        while current:
            if current.data == value:
                print("found the element")
                previous.next = current.next
                current.next = None
                deleted = True
                break

            else:
                previous = current
                current = current.next
        return deleted


new_list = LinkedList()
new_list.insert_at_tail('40')
new_list.insert_at_tail('60')
new_list.insert_at_tail('30')
new_list.insert_at_head('690')
new_list.search_element('30')
new_list.delete_node_by_value("690")
new_list.print_linkedlist()
