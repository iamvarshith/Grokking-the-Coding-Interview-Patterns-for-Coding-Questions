"""
Problem Statement#

Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
"""


def square_elemnts(arr):

    result_arr = [0 for i in range(len(arr))]
    left_pointer = 0
    square_index = len(arr) - 1
    right_pointer = len(arr) - 1
    while left_pointer <= right_pointer:
        squareleft = arr[left_pointer] * arr[left_pointer]
        squareright = arr[right_pointer] * arr[right_pointer]
        if squareleft > squareright:
            result_arr[square_index] = squareleft
            left_pointer += 1
        else:
            result_arr[square_index] = squareright
            right_pointer -= 1
        square_index -= 1
    return result_arr


print(square_elemnts([-2, -1, 0, 2, 3]))
