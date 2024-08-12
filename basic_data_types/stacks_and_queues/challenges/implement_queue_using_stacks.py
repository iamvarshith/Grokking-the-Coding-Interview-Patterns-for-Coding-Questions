from basic_data_types.stacks_and_queues.stacks.stacks import MyStack

class NewQueue:
    def __init__(self):
        self.main_stack = MyStack()
        # Write your code here


    # Inserts the element in the queue
    def enqueue(self, value):
        if self.main_stack.size() == 0:
            self.main_stack.stack(value)
        else:
            temp_stack = MyStack()
            for i in range(self.main_stack.size()):
                temp_val = self.main_stack.destack()
                temp_stack.stack(temp_val)
            self.main_stack.stack(value)
            for i in range(temp_stack.size()):
                temp_val = temp_stack.destack()
                self.main_stack.stack(temp_val)




    # Removes the element from the queue
    def dequeue(self):
        if self.main_stack.size() == 0:
            raise IndexError("dequeue from empty queue")
        return self.main_stack.destack()

if __name__ == "__main__":
    queue = NewQueue()
    queue.enqueue(-3)
    queue.enqueue(4)
    queue.enqueue(-9)
    queue.dequeue()
    print(queue.main_stack.peek())
