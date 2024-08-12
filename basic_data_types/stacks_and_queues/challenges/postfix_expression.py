"""
 Evaluate Postfix Expression Using a Stack

 Given a string, exp, represents an arithmetic expression in a postfix notation. Evaluate exp and return the resulting integer value.

The rules are given below:

The valid operators are '+', '-', '*', and '/'.

Each operand may be an integer or another expression.

The division between two integers always truncates toward zero.

There will not be any division by zero.

The input represents a valid arithmetic expression in a postfix notation.

The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""
import string

from basic_data_types.stacks_and_queues.stacks.stacks import MyStack


def postfix(exp: string):
    temp_stack = MyStack()
    operator_list = ["+","-","*","/"]
    for i in range(len(exp)):
        if exp[i] in operator_list:
            postfix_in_stack(exp[i],temp_stack)
        else:
            temp_stack.stack(int(exp[i]))

    return temp_stack.destack()


def postfix_in_stack(operator,stack):
    if operator == "+":
        val_1 = stack.destack()
        val_2 = stack.destack()
        stack.stack(val_1+val_2)
    if operator == "-":
        val_1 = stack.destack()
        val_2 = stack.destack()
        stack.stack(val_2 - val_1)

    if operator == "*":
        val_1 = stack.destack()
        val_2 = stack.destack()
        stack.stack(val_2 * val_1)

    if operator == "/":
        val_1 = stack.destack()
        val_2 = stack.destack()
        stack.stack(int(val_2 / val_1))

if __name__== "__main__":
    print(postfix("34*2+"))