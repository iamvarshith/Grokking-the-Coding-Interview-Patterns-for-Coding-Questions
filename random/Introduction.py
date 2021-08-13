""""Given an array, find the average of all contiguous subarrays of size ‘K’ in it."""


def average(k, array):
    result = []
    window_sum, windowstart = 0.00, 0
    for window_end in range(len(array)):
        window_sum += array[window_end]
        if window_end >= k-1:
            result.append(window_sum / k)  # calculate the average
            window_sum -= array[windowstart]  # subtract the element going out
            windowstart += 1  # slide the window ahead

    print(result)
Array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
average(k,Array)