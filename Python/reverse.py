class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT_32 = -2 ** 31
        MAX_INT_32 = 2 ** 31 - 1
        if MIN_INT_32 <= x <= MAX_INT_32:
            if(x%10==0):
                a=str(x)[:-1]
            a=str(x).replace('-', '')
            a=str(a)[::-1]
            if(x<0):
                a = '-'+a
            a=int(a)
            if MIN_INT_32 <= a <= MAX_INT_32:
                return (a)
        return 0
            
    
    
solution = Solution()

result = solution.reverse(1534236469)

print("Resultado: ",result)