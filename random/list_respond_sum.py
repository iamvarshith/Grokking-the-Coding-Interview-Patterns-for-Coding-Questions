def maxSlidingWindow(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    maxi = []
    sum_found = 0
    window_start = 0
    for window_end in range(len(nums)):
        sum_found = nums[window_end] + sum_found

        if window_end >= k - 1:
            print(sum_found, )
            maxi.append(sum_found)
            left_char = nums[window_start]
            sum_found -= left_char
            window_start += 1
    return maxi


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
