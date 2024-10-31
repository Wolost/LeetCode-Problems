from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set() 
        nums.sort()    
        n = len(nums)

        for i in range(n - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, n - 1  

            while j < k:
                s = nums[i] + nums[j] + nums[k]  

                if s == 0:
                    result.add((nums[i], nums[j], nums[k]))  
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1 
                    
        return [list(triplet) for triplet in result]
    
solution = Solution()

result = solution.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4])

print("Resultado: ",result)