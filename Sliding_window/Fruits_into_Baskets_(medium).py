"""Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""


def Fruits_into_Baskets_(array):
    start_window = 0
    max_length = 0
    max_fruits = {}
    for end_window in range(len(array)):
        if array[end_window] not in max_fruits:
            max_fruits[array[end_window]] = 0

        max_fruits[array[end_window]] += 1

        while len(max_fruits) > 2:
            max_fruits[array[start_window]] -= 1
            if max_fruits[array[start_window]] == 0:
                del max_fruits[array[start_window]]
            start_window += 1
        max_length = max(max_length, end_window - start_window + 1)
    return max_length


print(Fruits_into_Baskets_(['A', 'B', 'C', 'B', 'B', 'C']))
