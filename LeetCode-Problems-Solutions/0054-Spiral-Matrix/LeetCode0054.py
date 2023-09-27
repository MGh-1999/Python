""" LeetCode Problems: #54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1: Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]                    Output: [1,2,3,6,9,8,7,4,5]
Example 2: Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]           Output: [1,2,3,4,8,12,11,10,9,5,6,7] """

def spiralOrder(matrix):
    lst = []
    up, left, down, right = 0, 0, len(matrix)-1, len(matrix[0])-1
    while (up <= down and left <= right):
        for i in range(left,right+1):
            lst.append(matrix[up][i])
        up += 1
        if (up > down):
            break
        for j in range(up, down+1):
            lst.append(matrix[j][right])
        right -= 1
        if (left > right):
            break
        for i in reversed(range(left,right+1)):
            lst.append(matrix[down][i])
        down -= 1
        if (up > down):
            break
        for j in reversed(range(up,down+1)):
            lst.append(matrix[j][left])
        left += 1
        if (left > right):
            break
    return lst

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))