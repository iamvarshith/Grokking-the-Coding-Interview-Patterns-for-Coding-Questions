"""
Problem Statement #

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

Example 1:

Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Example 2:

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.

"""


def search_triplets(arr: list):
    triplet_list = []
    arr.sort()
    print(arr)
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_2sum(arr, i, triplet_list)
    return triplet_list


def search_2sum(arr, index, triplet_list):
    target_sum = -arr[index]

    start_pointer = index + 1
    end_pointer = len(arr) - 1

    while start_pointer < end_pointer:
        two_sum = arr[start_pointer] + arr[end_pointer]

        if two_sum < target_sum:
            start_pointer += 1
        elif two_sum > target_sum:
            end_pointer -= 1
        elif two_sum == target_sum:
            found = [arr[index], arr[start_pointer], arr[end_pointer]]
            triplet_list.append(found)
            start_pointer += 1
            end_pointer -= 1
            while start_pointer < end_pointer and arr[start_pointer] == arr[start_pointer - 1]:
                start_pointer += 1
            while start_pointer < end_pointer and arr[end_pointer] == arr[end_pointer + 1]:
                end_pointer -= 1


if __name__ == "__main__":
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
