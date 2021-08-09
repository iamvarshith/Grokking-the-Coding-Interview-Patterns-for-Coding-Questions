"""Given an array of positive numbers and a positive number ‘k,’
find the maximum sum of any contiguous subarray of size ‘k’."""

array = [2, 3, 4, 1, 5]
k = 2

sum_sum = 0
max_sum = 0
for i in range(k):
    sum_sum += array[i]

for j in range(len(array) - k):
    temp_sum = sum_sum

    temp_sum += array[j + k]
    temp_sum -= array[j]
    if temp_sum > sum_sum:
        sum_sum = temp_sum

print(sum_sum)
