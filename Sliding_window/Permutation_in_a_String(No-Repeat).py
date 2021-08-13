"""Given a string and a pattern, find out if the string contains any permutation of the pattern No repeat .

Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

    abc
    acb
    bac
    bca
    cab
    cba

If a string has ‘n’ distinct characters, it will have n!n!n! permutations.

Example 1:

Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.

Example 2:

Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.

Example 3:

Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.

Example 4:

Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern."""


def permutation(str1, pattern):
    k = len(pattern)
    window_start = 0
    pattern = set(pattern)

    for window_end in range(len(pattern) - 1, len(str1)):
        print(window_start, window_end,k)
        print(set(str1[window_start:window_end + 1]))
        print(pattern)
        if pattern == set(str1[window_start:window_end + 1]):
            return True
        else:
            window_start += 1



print(permutation('DDHDSSN', 'NHDSDDS'))
