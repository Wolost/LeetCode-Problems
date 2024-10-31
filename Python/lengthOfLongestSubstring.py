class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        response = 0
        n = len(s)
        for i in range(n):
            # Initializing all characters as not visited
            visited = [False] * 256
            
            for j in range(i, n):
                # If current character exist, break
                if visited[ord(s[j])] == True:
                    break
                else:
                    #loop the string and
                    response = max(response, j - i + 1)
                    visited[ord(s[j])] = True
                
        return response
            
solution = Solution()

result = solution.lengthOfLongestSubstring("geeksforgeeks")

print("Resultado: ",result)