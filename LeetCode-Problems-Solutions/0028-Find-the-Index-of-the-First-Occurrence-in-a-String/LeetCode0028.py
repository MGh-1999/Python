""" LeetCode Problems: #28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence
of needle in haystack, or -1 if needle is not part of haystack.

Example 1: Input: haystack = "sadbutsad", needle = "sad"
           Output: 0
Example 2: Input: haystack = "leetcode", needle = "leeto"
           Output: -1 """

def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    else:
        for index in range(len(haystack)): 
            if needle == haystack[index:index+len(needle)]: 
                return index

haystack = "sadbutsad"
needle = "sad"

print(strStr(haystack, needle))