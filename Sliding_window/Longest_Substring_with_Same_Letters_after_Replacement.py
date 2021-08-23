"""Problem Statement #

Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter,
find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc"."""


def Longest_Substring_with_Same_Letters_after_Replacement(str1, k):
    window_start = 0
    max_length = 0
    maxRepeatLetterCount = 0
    dictionary = {}

    for window_end in range(len(str1)):
        if str1[window_end] not in dictionary:
            dictionary[str1[window_end]] = 0
        dictionary[str1[window_end]] += 1
        maxRepeatLetterCount = max(maxRepeatLetterCount, dictionary[str1[window_end]])

        if (window_end - window_start + 1 - maxRepeatLetterCount) > k:
            dictionary[str1[window_start]] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


print(Longest_Substring_with_Same_Letters_after_Replacement("aabccbb", 2))
print(Longest_Substring_with_Same_Letters_after_Replacement("abbcb", 1))
print(Longest_Substring_with_Same_Letters_after_Replacement("aaacaa", 2))
