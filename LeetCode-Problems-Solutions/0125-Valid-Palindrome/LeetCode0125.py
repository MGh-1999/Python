""" LeetCode Problems: #125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1: Input: s = "A man, a plan, a canal: Panama"              Output: true
Example 2: Input: s = "race a car"                                  Output: false
Example 3: Input: s = " "                                           Output: true """

def isPalindrome(s):
    s = s.lower()
    converted_string = ''
    for i in range(len(s)):
        if s[i].isalnum():
            converted_string += s[i]
    for i in range(len(converted_string)//2):
        if (converted_string[i] != converted_string[len(converted_string)-1-i]):
            return False
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))