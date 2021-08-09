"""Problem Statement #

Given a string, find the length of the longest substring, which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".

Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".

Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde"."""


def No_repeat_Substring(string):
    start_pointer = 0
    max_till_Now = 0
    dictionary = {}
    for i in range(len(string)):
        print(i,start_pointer,max_till_Now,dictionary)
        if string[i] not in dictionary:
            dictionary[string[i]] = 0
        else:
            start_pointer += i
            max_till_Now = max(max_till_Now, len(dictionary))
            dictionary.clear()
            dictionary[string[i]] = 0
    return max_till_Now

print(No_repeat_Substring('abccde'))