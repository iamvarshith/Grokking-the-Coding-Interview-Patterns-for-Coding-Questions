"""
Problem Statement#

Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the
square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead,
they will be stuck in a cycle of numbers which does not include ‘1’.

"""

"""
Example 1:

Input: 23   
Output: true (23 is a happy number)  
Explanations: Here are the steps to find out that 23 is a happy number:

    22+322^2 + 3 ^22​2​​+3​2​​ = 4 + 9 = 13
    12+321^2 + 3^21​2​​+3​2​​ = 1 + 9 = 10
    12+021^2 + 0^21​2​​+0​2​​ = 1 + 0 = 1

Example 2:

Input: 12   
Output: false (12 is not a happy number)  
Explanations: Here are the steps to find out that 12 is not a happy number:

    12+221^2 + 2 ^21​2​​+   2​2​​ = 1 + 4 = 5
    525^25​2​​ = 25
    22+522^2 + 5^22​2​​+5​2​​ = 4 + 25 = 29
    22+922^2 + 9^22​2​​+9​2​​ = 4 + 81 = 85
    82+528^2 + 5^28​2​​+5​2​​ = 64 + 25 = 89
    82+928^2 + 9^28​2​​+9​2​​ = 64 + 81 = 145
    12+42+521^2 + 4^2 + 5^21​2​​+4​2​​+5​2​​ = 1 + 16 + 25 = 42
    42+224^2 + 2^24​2​​+2​2​​ = 16 + 4 = 20
    22+022^2 + 0^22​2​​+0​2​​ = 4 + 0 = 4
    424^24​2​​ = 16
    12+621^2 + 6^21​2​​+6​2​​ = 1 + 36 = 37
    32+723^2 + 7^23​2​​+7​2​​ = 9 + 49 = 58
    52+825^2 + 8^25​2​​+8 = 25 + 64 = 89

Step ‘13’ leads us back to step ‘5’ as the number becomes equal to ‘89’, this means that we can never reach ‘1’, therefore, ‘12’ is not a happy number.

"""


def happynumber(number):
    fast_pointer = number
    slow_pointer = number
    while True:
        slow_pointer = sum_square(slow_pointer)
        fast_pointer = sum_square(sum_square(fast_pointer))
        if slow_pointer == fast_pointer:
            break
    if slow_pointer==1:
        return True
    return False


def sum_square(number):
    sum_ = 0
    while number > 0:
        k = number % 10
        sum_ += k * k
        number = number // 10
    return sum_


print(happynumber(12))