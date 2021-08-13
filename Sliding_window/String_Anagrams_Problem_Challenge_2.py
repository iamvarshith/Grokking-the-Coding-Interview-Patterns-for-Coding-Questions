"""String Anagrams (hard) #

Given a string and a pattern, find all anagrams of the pattern in the given string.

Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N!N! permutations (or anagrams) of a string having NNN characters. For example, here are the six anagrams of the string “abc”:

    abc
    acb
    bac
    bca
    cab
    cba

Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

Example 2:

Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc"."""


def Anagrams(pattern,string1):
    list1 = []
    start_window = 0
    dict_pattern = {}
    list_index = []
    matched = 0

    for char in pattern:
        if char not in dict_pattern:
            dict_pattern[char] = 0
        dict_pattern[char] += 1

    for end_window in range(len(string1)):
        print(dict_pattern)
        print('matched  ' + str(matched), 'start  ' + str(start_window), 'end  ' + str(end_window))
        if string1[end_window] in dict_pattern:
            dict_pattern[string1[end_window]] -= 1
            if dict_pattern[string1[end_window]] == 0:
                matched += 1
        if matched == len(pattern):
            # print('matched  ' + str(matched),end_window)
            list_index.append(start_window)
        if end_window >= len(pattern) -1:
            left_elem = string1[start_window]
            start_window += 1
            # print(left_elem,end_window)
            if left_elem in dict_pattern:
                if dict_pattern[left_elem] == 0:
                    matched -= 1
                dict_pattern[left_elem] += 1

    return list_index


print(Anagrams("abc","abbcabc"))