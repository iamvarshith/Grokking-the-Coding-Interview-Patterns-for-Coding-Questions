"""Given an array of positive numbers and a positive number ‘k,’
find the maximum sum of any contiguous subarray of size ‘k’."""

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5

counter = 0
for j in range(k):
    counter += arr[j]


sub_arr = [counter/k]
for i in range(len(arr) - k):
    counter -= arr[i]
    counter += arr[i + k]
    sub_arr.append(counter/k)
    print(sub_arr)
