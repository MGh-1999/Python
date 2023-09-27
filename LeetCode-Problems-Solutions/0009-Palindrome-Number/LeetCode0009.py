""" LeetCode Problems: #9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1: Input: x = 121               Output: true
Example 2: Input: x = -121              Output: false
Example 3: Input: x = 10                Output: false """

def isPalindrome(x):
    if (x >= 0):
        number = x
        reversed_number = 0
        while (number > 0):
            last_digit = number % 10
            reversed_number = reversed_number*10 + last_digit
            number //= 10
        return x == reversed_number
    else:
        return False

x = 121
print(isPalindrome(x))