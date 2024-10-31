from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()    
        n = len(nums)
        if(n < 3):
            return 0
        
        result = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            
            j, k = i + 1, n - 1 
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]  
                
                if(s == target):
                    return s
                
                if abs(s - target) < abs(result - target):
                    result = s

                if s < target:
                    j += 1
                else:
                    k -= 1
                
        return result

solution = Solution()

result = solution.threeSumClosest([0,0,0], 1)

print("Resultado: ",result)