""" LeetCode Problems: #50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

Example 1: Input: x = 2.00000, n = 10           Output: 1024.00000
Example 2: Input: x = 2.10000, n = 3            Output: 9.26100
Example 3: Input: x = 2.00000, n = -2           Output: 0.25000 """

def myPow(x, n):
    if (n>=0):
        result = 1
        for i in range(n):
            result *= x
        return result
    else:
        result = 1
        for i in range(-n):
            result /= x
        return result

x = 2
n = 10
print(myPow(x, n))