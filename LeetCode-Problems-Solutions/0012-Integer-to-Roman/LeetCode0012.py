""" LeetCode Problems: #12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral.

Example 1: Input: num = 3               Output: "III"
Example 2: Input: num = 58              Output: "LVIII"
Example 3: Input: num = 1994            Output: "MCMXCIV"

Constraints: 1 <= num <= 3999 """

def intToRoman(num):
    decomposition = []
    i = 0
    while (num > 0):
        last_digit = num % 10
        decomposition.insert(0, last_digit * 10**i)
        num //= 10
        i += 1
    dictionary = {3000:'MMM', 2000:'MM', 1000:'M',
        900:'CM', 800:'DCCC', 700:'DCC', 600:'DC', 500:'D', 400:'CD', 300:'CCC', 200:'CC', 100:'C',
        90:'XC', 80:'LXXX', 70:'LXX', 60:'LX', 50:'L', 40:'XL', 30:'XXX', 20:'XX', 10:'X',
        9:'IX', 8:'VIII', 7:'VII', 6:'VI', 5:'V', 4:'IV', 3:'III', 2:'II', 1:'I', 0: ''}
    roman = ''
    for key in decomposition:
        roman += dictionary[key]
    return roman

num = 3
print(intToRoman(num))