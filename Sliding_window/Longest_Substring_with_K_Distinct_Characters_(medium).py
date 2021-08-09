"""Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string."""
import math


def Longest_Substring_with_K_Distinct_Characters(string, k):
    max_size = 0
    window_start = 0
    hashmap = {}
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in hashmap:
            hashmap[right_char] = 0
        hashmap[right_char] += 1

        while len(hashmap) > k:
            hashmap[string[window_start]] -= 1
            if hashmap[string[window_start]] == 0:
                del hashmap[string[window_start]]

            window_start += 1
            max_size = max(max_size, window_end - window_start + 1)
    return max_size


string = "araaci"
k = 2

print(Longest_Substring_with_K_Distinct_Characters(string, k))
