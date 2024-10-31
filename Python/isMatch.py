import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if (re.search(re.compile(f"^{p}$"), s)): return True 
        else: return False
        


solution = Solution()

result = solution.isMatch("aa","a")

print("Resultado: ",result)