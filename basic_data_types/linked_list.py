class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current_head = self.head
            while current_head.next:
                current_head = current_head.next
            current_head.next = new_node
        else:
            self.head = new_node

    def print_linkedList(self):
        current = self.head
        while current:
            print(current.data, current.next)
            current = current.next

    def find_node(self, node_data):
        if self.head:
            fast_pointer = self.head
            while fast_pointer:
                if fast_pointer.data == node_data:
                    return fast_pointer
                else:
                    fast_pointer = fast_pointer.next

    def circular_linked_list(self, node_data):
        found_node = Linkedlist.find_node(self,node_data)
        if self.head:
            current_head = self.head
            while current_head.next:
                current_head = current_head.next
            current_head.next = found_node
        else:
            self.head = found_node


Linkedlist()
