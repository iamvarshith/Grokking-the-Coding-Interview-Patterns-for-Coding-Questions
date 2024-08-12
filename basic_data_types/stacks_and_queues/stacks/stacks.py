class MyStack:
    def __init__(self):
        self.stack_list = []
        self.stack_size = 0

    def is_empty(self):
        return self.stack_size == 0

    def peek(self):
        if self.is_empty():
            return None
        return self.stack_list[-1]

    def size(self):
        return self.stack_size

    def stack(self, value):
        self.stack_list.append(value)
        self.stack_size += 1

    def destack(self):
        if self.stack_size >0:
            value = self.stack_list.pop()
            self.stack_size -= 1
            return value
        else:
            return False

if __name__ == "__main__":
    stack_obj = MyStack()
    print("is_empty(): " + str(stack_obj.is_empty()))
    print("peek(): " + str(stack_obj.peek()))
    print("size(): " + str(stack_obj.size()))
