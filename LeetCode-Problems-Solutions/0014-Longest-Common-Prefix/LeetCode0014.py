""" LeetCode Problems: #14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1: Input: strs = ["flower","flow","flight"]             Output: "fl"
Example 2: Input: strs = ["dog","racecar","car"]                Output: "" """

def longestCommonPrefix(strs):
    longest_common_prefix = ''
    for i in range(len(strs[0])):
        valid = True
        for j in range(1,len(strs)):
            if (strs[0][i] != strs[j][i]):
                valid = False
                break
        if valid:
            longest_common_prefix += strs[0][i]
        else:
            break
    return longest_common_prefix

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))