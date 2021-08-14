"""Smallest Window containing Substring (hard) #

Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"

Example 2:

Input: String="abdbca", Pattern="abc"
Output: "bca"
Explanation: The smallest substring having all characters of the pattern is "bca".

Example 3:

Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern."""

def smallest_window(string1,pattern):
    start_window = 0
    dict_pattern= {}
    matched = 0
    start_index = 0
    end_index = 0


    for char in pattern:
        if char not in dict_pattern:
            dict_pattern[char] = 0
        dict_pattern[char] += 1

    for end_window in range(len(string1)):
        if string1[end_window] in dict_pattern:
            dict_pattern[string1[end_window]] -= 1
            if dict_pattern[string1[end_window]] >= 0:
                matched += 1

        while matched == len(pattern):
            start_index = start_window
            end_index = end_window
            if end_window - start_window == len(pattern) -1:
                start_index = start_window
                end_index = end_window
                return string1[start_index:end_index+1]
            left_char = string1[start_window]
            start_window += 1
            start_index += 1
            if left_char in dict_pattern:
                if dict_pattern[left_char] == 0:
                    matched -= 1
                dict_pattern[left_char] += 1
        # print(end_window,matched)
        # while end_window == len(string1)-1:
        #
        #     if matched == len(pattern):
        #
        #         if end_window - start_window == len(pattern)-1:
        #
        #             start_index = start_window
        #             end_index = end_window
        #         if end_window - start_window > len(pattern)-1:
        #
        #             if string1[start_window] in dict_pattern and dict_pattern[string1[start_window]] < 0:
        #                 print(end_window, matched)
        #                 start_index = start_window
        #                 end_index = end_window
        #                 print(dict_pattern)
        #                 return start_index,end_index
        #             dict_pattern[string1[start_window]] += 1
        #             print( dict_pattern)
        #             start_index += 1

    return string1[start_index:end_index+1]


print(smallest_window('abdbca','abc'))