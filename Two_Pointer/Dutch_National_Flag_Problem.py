"""Problem Statement#

Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects,
hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and since our input array also consists of
three different numbers that is why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0, 0, 1, 1, 2]

Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0, 0, 1, 2, 2, 2,]
"""

"""
 So the idea is to solve, We can use a Two Pointers approach while iterating through the array. Let’s say the two
 pointers are called low and high which are pointing to the first and the last element of the array respectively. 
 So while iterating, we will move all 0s before low and all 2s after high so that in the end, all 1s will be between 
 low and high.
 """


def dutch_flag(lst):
    lower_pointer = 0
    high_pointer = len(lst) - 1
    iteration_pointer = 0

    while iteration_pointer <= high_pointer:
        if lst[iteration_pointer] == 1:
            iteration_pointer += 1
        elif lst[iteration_pointer] == 0:
            lst[lower_pointer], lst[iteration_pointer] = lst[iteration_pointer], lst[lower_pointer]
            lower_pointer += 1
            iteration_pointer += 1
        elif lst[iteration_pointer] == 2:
            lst[high_pointer], lst[iteration_pointer] = lst[iteration_pointer], lst[high_pointer]
            high_pointer -= 1
    return lst


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag(arr)
    print(arr)


"""
Solution be like this.
[0, 0, 1, 1, 2]
[0, 0, 1, 2, 2, 2]
"""

if __name__ == "__main__":
    main()
