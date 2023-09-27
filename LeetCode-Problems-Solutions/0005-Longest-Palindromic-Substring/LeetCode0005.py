""" LeetCode Problems: #5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1: Input: s = "babad"           Output: "bab"
Example 2: Input: s = "cbbd"            Output: "bb" """

def longestPalindrome(s):
    longest_palindromic_subtring = ''
    for i in range(len(s)):
        substring = ''
        for j in range(i,len(s)):
            substring += s[j]
            valid  = True if (substring[:] == substring[::-1]) else False
            if valid:
                if (len(substring) > len(longest_palindromic_subtring)):
                    longest_palindromic_subtring = substring[:]
    return longest_palindromic_subtring

s = "babad"
print(longestPalindrome(s))