from basic_data_types.stacks_and_queues.queues.queue import MyQueue
from basic_data_types.stacks_and_queues.stacks.stacks import MyStack


def reverse_first_k_elements_in_queue(queue: MyQueue, k : int):
    """

    :param k:
    :type queue: object
    """

    if k <= 0 or queue.size() == 0 or k > queue.size():
        return None

    temp_stack = MyStack()
    for i in range(k):
        value = queue.dequeue()
        temp_stack.stack(value)
    while temp_stack.size() > 0:
        temp_value = temp_stack.destack()
        queue.enqueue(temp_value)

    for i in range(queue.size() - k):
        temp_value = queue.dequeue()
        queue.enqueue(temp_value)

    return queue

if __name__ == "__main__":
    queue = MyQueue()
    for x in [2,-4,-3,-7,-8] :
        queue.enqueue(x)
    responce = reverse_first_k_elements_in_queue(queue,-8)

