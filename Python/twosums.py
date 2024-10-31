from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in hashmap:
                print([hashmap[complemento], i])
            hashmap[num] = i  


solution = Solution()

result = solution.twoSum([3,2,4],6)

print("Resultado: ",result)