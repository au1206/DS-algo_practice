"""
LC7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
-231 <= x <= 231 - 1
"""


# Solution 1
class Solution:
    def reverse(self, x: int) -> int:
        digits = []
        res = 0
        negative = False
        if x < 0:
            negative = True
            x *= -1

        while x > 0:
            digits.append(x % 10)
            x = x // 10

        i = len(digits) - 1
        for digit in digits:
            res += digit * (10 ** i)
            i -= 1
        if negative:
            res *= -1
        if not -2 ** 31 <= res <= (2 ** 31) - 1:
            res = 0
        return res


# Solution 2
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        res = ""
        if x[0] != '-':
            res = int(x[::-1])

        else:
            x = x[1:]
            res = int('-' + x[::-1])

        if not -2 ** 31 <= res <= (2 ** 31) - 1:
            res = 0

        return res
