import sys

class Solution:
    def myAtoi(self, s: str) -> int:
        i, base, sign = 0, 0, 1
        MIN_INT_32 = -2 ** 31
        MAX_INT_32 = 2 ** 31 - 1
     
        # Ignore leading whitespace
        s = s.lstrip()

        # Handle sign if present
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Parse digits until a non-digit character is encountered
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before adding the digit
            if base > (MAX_INT_32 - digit) // 10:
                return MAX_INT_32 if sign == 1 else MIN_INT_32
            
            base = base * 10 + digit
            i += 1
        
        return max(MIN_INT_32, min(sign * base, MAX_INT_32))   

solution = Solution()

result = solution.myAtoi("   +0 123")

print("Resultado: ",result)