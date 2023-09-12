""" LeetCode Problems: #66. Plus One

You are given a large integer represented as an integer array digits, where 
each digits[i] is the ith digit of the integer. The digits are ordered 
from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1: Input: digits = [1,2,3]              Output: [1,2,4]
Example 2: Input: digits = [4,3,2,1]            Output: [4,3,2,2]
Example 3: Input: digits = [9]                  Output: [1,0] """

def plusOne(digits):
    every_digit_is_nine = True
    for i in range(len(digits)):
        if (digits[i] != 9):
            every_digit_is_nine = False
    if (every_digit_is_nine == True):
        digits.insert(0,0)
    i = len(digits)-1
    while (digits[i] == 9):
        digits[i] = 0
        i -= 1
    digits[i] += 1
    return digits

digits = [1,2,3]
print(plusOne(digits))