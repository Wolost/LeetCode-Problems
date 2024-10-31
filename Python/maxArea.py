from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        lp, rp= 0,  (len(height)-1)
        area = [0] * (len(height)-1)
        
        while i <= (len(height)-1):
            if(lp == rp):break
            left = height[lp]
            right = height[rp]
            
            area[i] = (min(left,right) * (rp-lp)) 
            
            rp -= 1 if left > right else 0
            lp += 1 if left <= right else 0
            
            i+=1
        return max(area)
solution = Solution()

result = solution.maxArea([1,1])

print("Resultado: ",result)