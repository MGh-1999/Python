""" LeetCode Problems: #187. Repeated DNA Sequences

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.

When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) 
that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1: Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"            Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2: Input: s = "AAAAAAAAAAAAA"                               Output: ["AAAAAAAAAA"] """

def findRepeatedDnaSequences(s):
    sequences_that_occur_more_than_once = []
    for i in range(0,len(s)-9):
        if ((s[i:i+10] in s[i+1:]) and (s[i:i+10] not in sequences_that_occur_more_than_once)):
            sequences_that_occur_more_than_once.append(s[i:i+10])
    return sequences_that_occur_more_than_once

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(s))