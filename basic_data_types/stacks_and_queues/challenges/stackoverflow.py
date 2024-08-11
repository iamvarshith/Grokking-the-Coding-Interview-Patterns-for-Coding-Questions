"""
Design a data structure TwoStacks, that represents two stacks using a single list, where both stacks share the same list for storing elements.

The following operations must be supported:

push1(value): Takes an integer value and inserts it into the first stack.

push2(value): Takes an integer value and inserts it into the second stack.

pop1(): Removes the top element from the first stack and returns it.

pop2(): Removes the top element from the second stack and returns it.


"""


class TwoStacks:
    def __int__(self, n):
        self.size = n
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = self.size

    def push1(self, value):
        if self.top1 < (self.top2 - 1):
            self.top1 += 1
            self.arr[self.top1] = value
        else:
            print("Stack Overflow")

    def push2(self, value):
        if self.top2 > self.top1 + 1:
            self.top2 -= 1
            self.arr[self.top2] = value
        else:
            print("Stack Overflow")

    def pop1(self):
        if self.top1 >= 0:
            value = self.arr[self.top1]
            self.top1 -= 1
            return value
        else:
            print("Stack Underflow ")
            exit(1)

    def pop2(self):
        # Return and remove top element from stack 2 if not empty, else print stack underflow and exit
        if self.top2 < self.size:
            value = self.arr[self.top2]
            self.top2 += 1
            return value
        else:
            print("Stack Underflow ")
            exit()