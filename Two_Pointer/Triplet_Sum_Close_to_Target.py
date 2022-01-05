"""
Problem Statement#

Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target
number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the
triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

"""
import math


def triplet_closest_sum(array: list, target: int):
    array.sort()
    smallest_diffrence = math.inf
    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1
        while left < right:
            target_diffence  = target - array[i] + array[left] + array[right]
            if target_diffence == 0:
                return target - target_diffence




