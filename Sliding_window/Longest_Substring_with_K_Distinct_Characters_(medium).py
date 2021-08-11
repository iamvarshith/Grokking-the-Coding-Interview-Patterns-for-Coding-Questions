"""Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.
Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Example 4:

Input: String="cbbebi", K=10
Output: 6
Explanation: The longest substring with no more than '10' distinct characters is "cbbebi".
"""
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
