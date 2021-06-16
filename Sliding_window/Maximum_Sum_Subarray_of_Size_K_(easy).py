"""Given an array of positive numbers and a positive number ‘k,’
find the maximum sum of any contiguous subarray of size ‘k’."""

array = [2, 1, 5, 1, 3, 2]
k = 3

sum = 0
max_sum = 0
for i in range(k):
    sum += array[i]

for j in range(len(array)-k):
    temp_sum = sum
    array[j+k]