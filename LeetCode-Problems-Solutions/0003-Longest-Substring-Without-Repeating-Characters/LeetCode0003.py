""" LeetCode Problems: #3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1: Input: s = "abcabcbb"            Output: 3
Example 2: Input: s = "bbbbb"               Output: 1
Example 3: Input: s = "pwwkew"              Output: 3 """

def lengthOfLongestSubstring(s):
    longest_substring_without_repeating_characters = ''
    for i in range(len(s)):
        substring = ''
        for j in range(i,len(s)):
            substring += s[j]
            valid  = True
            for k in range(len(substring)):
                if (substring[k] in substring[:k]+substring[k+1:]):
                    valid = False
            if valid:
                if (len(substring) > len(longest_substring_without_repeating_characters)):
                    longest_substring_without_repeating_characters = substring[:]
            else:
                break
    return len(longest_substring_without_repeating_characters)

s = "abcabcbb"
print(lengthOfLongestSubstring(s))