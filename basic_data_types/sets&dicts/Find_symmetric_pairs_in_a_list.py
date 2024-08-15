"""
Given a list of pairs, nums, find all the symmetric pairs from it. If no symmetric pair is found, return an empty list.
"""


def find_symmetric(nums):
    nums_set = set()
    results_list = []
    for pairs in nums:
        current_pair = tuple(pairs)
        pairs.reverse()
        reverse_pair = tuple(pairs)
        if reverse_pair in nums_set:
            results_list.append(list(current_pair))
            results_list.append((list(reverse_pair)))
        else:
            nums_set.add(current_pair)
    print(results_list)


if __name__ == "__main__":
    find_symmetric([[1,2],[4,6],[4,3],[6,4],[5,9],[3,4],[9,5]])