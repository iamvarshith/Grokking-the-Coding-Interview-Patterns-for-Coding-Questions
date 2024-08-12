from basic_data_types.stacks_and_queues.stacks.stacks import MyStack


def sort_stacks(stack: MyStack):
    if stack.size() == 0:
        return "No can do bro"

    temp_stack = MyStack()
    while stack.size() > 0:
        # Pop the top element from the original stack
        current = stack.destack()

        # While the temporary stack is not empty and the top element is greater than the current element
        while temp_stack.size() > 0 and temp_stack.peek() > current:
            # Pop from temporary stack and push back to the original stack
            stack.stack(temp_stack.destack())

        # Push the current element to the temporary stack
        temp_stack.stack(current)

    # Now transfer back the elements to the original stack
    while temp_stack.size() > 0:
        stack.stack(temp_stack.destack())

    return stack


if __name__ == "__main__":
    new_stack = MyStack()
    for i in [1, 9, 2]:
        new_stack.stack(i)

    sorted_stack = sort_stacks(new_stack)
    # Print the sorted stack elements
    while sorted_stack.size() > 0:
        print(sorted_stack.destack())
