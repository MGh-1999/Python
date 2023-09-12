""" LeetCode Problems: #118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1: Input: numRows = 5           Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2: Input: numRows = 1           Output: [[1]] """

def generate(numRows):
    PascalTriangle = []
    for i in range(numRows):
        newLine = []
        for j in range(i+1):
            if ((j==0) or (j==i)):
                newLine.append(1)
            else:
                newLine.append(PascalTriangle[-1][j-1]+PascalTriangle[-1][j])
        PascalTriangle.append(newLine)
    return PascalTriangle

numRows = 5
print(generate(numRows))