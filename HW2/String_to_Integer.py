class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Ignore leading whitespace
        i = 0
        n = len(s)
        while i < n and s[i] == ' ':
            i += 1

        # If all characters are whitespace, return 0
        if i == n:
            return 0

        # Step 2: Determine if there is a sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Step 3: Convert characters to an integer
        result = 0
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1

        # Apply the sign
        result *= sign

        # Step 4: Clamp the result within the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
