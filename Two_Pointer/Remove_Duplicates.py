"""Problem Statement #

Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing
the duplicates in-place return the length of the subarray that has no duplicate in it.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11]."""


# This is will give you the solution but will not change the list !. So the tak in hand is to change the array
#
# def remove_duplicates(arr):
#     duplicates = 0
#
#     for pointer_start in range(1, len(arr)):
#         pointer_end = pointer_start - 1
#         if arr[pointer_start] == arr[pointer_end]:
#             duplicates += 1
#     return len(arr) - duplicates
#
#
# print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
# print(remove_duplicates([2, 2, 2, 11]))

def remove_duplicates(arr):
    non_duplicate = 1
    pointer = 1
    while (pointer < len(arr)):
        if arr[non_duplicate - 1] != arr[pointer]:
            arr[non_duplicate] = arr[pointer]
            non_duplicate += 1
    return non_duplicate
