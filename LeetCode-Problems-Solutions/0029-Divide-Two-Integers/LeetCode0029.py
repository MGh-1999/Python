""" LeetCode Problems: #29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using 
multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Constraints:
-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0

Example 1: Input: dividend = 10, divisor = 3            Output: 3
Example 2: Input: dividend = 7, divisor = -3            Output: -2 """

def divide(dividend, divisor):
    if (dividend >= 0 and divisor > 0):
        greatest_multiple_of_divisor_less_than_or_equal_to_dividend = 0
        quotient, remainder = 0, dividend
        while (remainder >= divisor):
            greatest_multiple_of_divisor_less_than_or_equal_to_dividend += divisor
            quotient += 1
            remainder -= divisor
        return quotient
    if (dividend >= 0 and divisor < 0):
        return -divide(dividend, -divisor)
    if (dividend < 0 and divisor > 0):
        return -divide(-dividend, divisor)
    if (dividend < 0 and divisor < 0):
        return divide(-dividend, -divisor)

dividend, divisor = 10, 3
print(divide(dividend, divisor))