""" LeetCode Problems: #263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1: Input: n = 6             Output: true
Example 2: Input: n = 1             Output: true
Example 3: Input: n = 14            Output: false """

def isUgly(n):
    if (n <= 0):
        return False
    for i in range(7,n+1):
        i_isPrime = True
        for j in range(2,i):
            if (i % j == 0):
                i_isPrime = False
                break
        if (i_isPrime and n % i == 0):
            return False
    return True

n = 6
print(isUgly(n))