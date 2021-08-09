"""Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray
whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists. """
import math


def smallest_subarray_with_a_given_sum(array, s):
    windowsum = 0
    window_start = 0
    min_len = math.inf

    # write a loop And note I is End of the window

    for i in range(len(array)):
        # Add first element in the first element in each iteration
        windowsum += array[i]
        # if the sum is grater or equal Then you Note the min lenth first. And delete the element from the sum and push
        # the windows to the second element
        while windowsum >= s:
            min_len = min(min_len, i - window_start + 1)
            windowsum -= array[window_start]
            window_start += 1
    if min_len == math.inf:
        return 0
    return min_len


print(smallest_subarray_with_a_given_sum([2, 1, 5, 2, 3, 2], 7))
