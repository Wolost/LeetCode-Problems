class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        response = 0
        n = len(s)
        for i in range(n):
            visited = [False] * 256
            
            for j in range(i, n):
                if visited[ord(s[j])] == True:
                    break
                else:
                    response = max(response, j - i + 1)
                    visited[ord(s[j])] = True
                
        return response
            
solution = Solution()

result = solution.lengthOfLongestSubstring("geeksforgeeks")

print("Resultado: ",result)