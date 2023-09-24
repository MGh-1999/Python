""" LeetCode Problems: #151. Reverse Words in a String

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. 
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. 
The returned string should only have a single space separating the words. 
Do not include any extra spaces.

Example 1: Input: s = "the sky is blue"             Output: "blue is sky the"
Example 2: Input: s = "  hello world  "             Output: "world hello"
Example 3: Input: s = "a good   example"            Output: "example good a" """

def reverseWords(s):
    list_of_words = []
    word = ''
    for i in range(len(s)):
        if (s[i] != ' '):
            word += s[i]
        else:
            if (word != ''):
                list_of_words.append(word)
                word = ''
    if (word != ''):
        list_of_words.append(word)
    reversed_string = ''
    for i in reversed(range(1,len(list_of_words))):
        reversed_string += list_of_words[i] + ' '
    reversed_string += list_of_words[0]
    return reversed_string

s = "the sky is blue"
print(reverseWords(s))