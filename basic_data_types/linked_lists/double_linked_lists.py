from single_linked_lists import LinkedList, Node


class MultipleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.previous = None


class DoubleLinkedList(LinkedList):
    def print_linkedlist(self):
        print("From new fun")
        current = self.head
        while current:
            print(current.previous,current.data, current.next)
            current = current.next






if __name__ == "__main__":
    new_list = DoubleLinkedList()
    new_list.insert_at_tail('40')
    new_list.insert_at_tail('60')
    new_list.insert_at_tail('30')
    new_list.insert_at_head('690')
    new_list.search_element('30')
    new_list.delete_node_by_value("690")
    new_list.print_linkedlist()
