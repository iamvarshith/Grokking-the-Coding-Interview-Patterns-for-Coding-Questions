"""
Challenge: A List as a Subset of Another List
Try to solve the A List as a Subset of Another List problem.

Statement
Given two lists, list1 and list2, implement a function that takes the two lists as input and checks whether list2 is a subset of list1.


"""


def is_subset(list1, list2):
    set_list1 = set(list1)
    for element in list2:
        if element not in set_list1:
            return False
    return True


if __name__ == "__main__":
    print(is_subset([9,4,7,1,-2,6,5],[7,1,-2]))