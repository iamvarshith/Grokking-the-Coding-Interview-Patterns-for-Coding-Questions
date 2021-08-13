"""Given a string and a pattern, find out if the string contains any permutation of the pattern.

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
    matched = 0
    char_frequency = {}

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0

        char_frequency[char] += 1

    for window_end in range((len(str1))):
        if str1[window_end] in char_frequency:
            char_frequency[str1[window_end]] -= 1
            if char_frequency[str1[window_end]] == 0:
                matched += 1
        if matched == len(char_frequency):
            return True

        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return False


print('Permutation exist: ' + str(permutation("TCKABC", "ABC")))
print('Permutation exist: ' + str(permutation("odicf", "dc")))
print('Permutation exist: ' + str(permutation("bcdxabcdy", "bcdyabcdx")))
print('Permutation exist: ' + str(permutation("aaacb", "abc")))
