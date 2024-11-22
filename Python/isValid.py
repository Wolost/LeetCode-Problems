class Solution:
    def isValid(self, s: str) -> bool:
        symbol_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for c in s:
            if c in symbol_map.values():
                stack.append(c)
            elif c in symbol_map.keys():
                if not stack or stack[-1] != symbol_map[c]:
                    return False
                stack.pop()
            else: return False
        return not stack
    
solution = Solution()

result = solution.isValid("()[]{}")

print("Resultado: ",result)