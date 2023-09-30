""" LeetCode Problems: #172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Constraints: 0 <= n <= 10**4

Example 1: Input: n = 3             Output: 0
Example 2: Input: n = 5             Output: 1
Example 3: Input: n = 0             Output: 0 """

def trailingZeroes(n):
    if (n // 5 == 0):
        return 0
    else:
        return n // 5 + trailingZeroes(n // 5)

n = 3
print(trailingZeroes(n))