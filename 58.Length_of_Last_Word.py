class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend < 0 and divisor > 0:
            s = abs(dividend) // divisor
            return -s
        elif dividend > 0 and divisor < 0:
            s = dividend // abs(divisor)
            return -s 
        elif dividend == -2147483648 and divisor == -1:
            return 2147483647
        else:
            return dividend // divisor

        