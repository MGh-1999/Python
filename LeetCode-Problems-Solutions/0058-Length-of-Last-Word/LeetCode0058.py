""" LeetCode Problems: #58. Length of Last Word

Given a string s consisting of words and spaces, return the length 
of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1: Input: s = "Hello World"                             Output: 5
Example 2: Input: s = "   fly me   to   the moon  "             Output: 4
Example 3: Input: s = "luffy is still joyboy"                   Output: 6 """

def lengthOfLastWord(s):
    length = 0
    for i in reversed(range(len(s))):
        if (length == 0):
            if (s[i] != ' '):
                length += 1
        else:
            if (s[i] != ' '):
                length += 1
            else:
                return length
    return length

s = "Hello World"
print(lengthOfLastWord(s))