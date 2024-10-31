from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        count = len(strs)
        prefx= [""]*count
        if (count > 1):
            aux = list(strs[0])
            while i < count:
                for char in strs[i]:
                    if(char in aux):
                        prefx[i] += char
                    else:
                        break
                i += 1
            return min(prefx)
        else:    
            return strs[0]

solution = Solution()

result = solution.longestCommonPrefix(["reflower","flow","flight"])

print("Resultado: ",result)