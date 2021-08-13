"""Problem Statement #

Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9."""


def longest_string_replace_0_1(arr, k):
    max_size = 0
    start_window = 0
    max_of_1 = 0
    dic = {}

    for end_window in range(len(arr)):
        if arr[end_window] not in dic:
            dic[arr[end_window]] = 0
        dic[arr[end_window]] += 1
        print(dic,start_window,end_window)
        max_of_1 = max(dic[arr[end_window]], max_of_1)

        if end_window - start_window + 1 - max_of_1 > k:
            dic[arr[start_window]] -= 1
            start_window += 1

        max_size = max(max_size, end_window - start_window + 1)
    return max_size


print(longest_string_replace_0_1([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2))
