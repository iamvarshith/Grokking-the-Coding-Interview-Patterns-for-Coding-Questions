from basic_data_types.linked_lists.double_linked_lists import DoublyLinkedList



class MyQueue:
    def __init__(self):
        self.items = DoublyLinkedList()

    def is_empty(self):
        return self.items.length == 0

    def front(self):
        if self.is_empty():
            return None
        else:
            return self.items.get_head()

    def rear(self):
        if self.is_empty():
            return None
        else:
            return self.items.get_tail()

    def size(self):
        return self.items.length

    def enqueue(self, value):
        return self.items.insert_tail(value)

    def dequeue(self):
        return self.items.remove_head()

queue_obj = MyQueue()