class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        if x == x[::-1]: return True 
        else: return False
    
    
solution = Solution()

result = solution.isPalindrome(10)

print("Resultado: ",result)