""" LeetCode Problems: #326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3^x.

Example 1: Input: n = 27            Output: true
Example 2: Input: n = 0             Output: false
Example 3: Input: n = -1            Output: false """

def isPowerOfThree(n):
    if (n <= 0):
        return False
    else:
        i = 0
        while (3**i <= n):
            if (3**i != n):
                i += 1
            else:
                return True
        return False

n = 27
print(isPowerOfThree(n))