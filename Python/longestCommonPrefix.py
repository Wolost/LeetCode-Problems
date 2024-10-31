from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefx = strs[0]
        
        for s in strs[1:]:
            while not s.startswith(prefx):
                prefx = prefx[:-1]
                if not prefx:
                    return ""

        return prefx

solution = Solution()

result = solution.longestCommonPrefix(["reflower","flow","flight"])

print("Resultado: ",result)