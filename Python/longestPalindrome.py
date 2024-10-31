class Solution:
    def longestPalindrome(self, s: str) -> str:
        T = '#'.join(f'^{s}$')
        n = len(T)
        
        P = [0] * n
        C = 0
        R = 0
        max_length = 0
        center_index = 0

        for i in range(1, n - 1):
            i_mirror = 2 * C - i
            
            if i < R:
                P[i] = min(R - i, P[i_mirror])
            
            while T[i + P[i] + 1] == T[i - P[i] - 1]:
                P[i] += 1
            
            if i + P[i] > R:
                C = i
                R = i + P[i]
            
            if P[i] > max_length:
                max_length = P[i]
                center_index = i

        start = (center_index - max_length) // 2
        
        return s[start: start + max_length]

solution = Solution()

result = solution.longestPalindrome("babad")

print("Resultado: ",result)