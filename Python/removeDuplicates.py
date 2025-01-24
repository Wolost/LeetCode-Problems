from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicatedMap = {}
        result = []
        
        for i in nums:
            duplicatedMap[i] = duplicatedMap.get(i,0)+1
        
        for key, value in duplicatedMap.items():
            if value >= 1:
                result.append(key)
        if not result:
            result.append(-1)
        
        nums[:len(result)] = result
        
        return len(result)


solution = Solution()

result = solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

print("Resultado: ",result)