class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None
        self.previous_element = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_head(self):
        if (self.head != None):
            return self.head.data
        else:
            return False

    def is_empty(self):
        if (self.head is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_tail(self, element):
        temp_node = Node(element)
        if (self.is_empty()):
            self.head = temp_node
            self.tail = temp_node
        else:
            self.tail.next_element = temp_node
            temp_node.previous_element = self.tail
            self.tail = temp_node
        self.length += 1
        return temp_node.data

    def remove_head(self):
        if (self.is_empty()):
            return False
        nodeToRemove = self.head;
        if (self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = nodeToRemove.next_element
            self.head.previous_element = None
            nodeToRemove.next_element = None
        self.length -= 1
        return nodeToRemove.data

    def get_tail(self):
        if (self.head != None):
            return self.tail.data
        else:
            return False

    def __str__(self):
        val = ""
        if (self.is_empty()):
            return ""
        temp = self.head
        val = "[" + str(temp.data) + ", "
        temp = temp.next_element

        while (temp.next_element):
            val = val + str(temp.data) + ", "
            temp = temp.next_element
        val = val + str(temp.data) + "]"
        return val