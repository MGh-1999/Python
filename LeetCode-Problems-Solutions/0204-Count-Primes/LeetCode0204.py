""" LeetCode Problems: #204. Count Primes

Given an integer n, return the number of prime numbers that are strictly less than n.

Constraints: 0 <= n <= 5 * 10**6

Example 1: Input: n = 10            Output: 4
Example 2: Input: n = 0             Output: 0
Example 3: Input: n = 1             Output: 0 """

from math import sqrt, ceil

def countPrimes(n):
    list_of_primes = [True]*n
    list_of_primes[0:2] = [False, False]
    for i in range(2, ceil(sqrt(n))):
        if (list_of_primes[i] == True):
            for j in range(i*i, n, i):
                list_of_primes[j] = False
    return len([i for i in range(n) if list_of_primes[i] == True])

n = 10
print(countPrimes(n))