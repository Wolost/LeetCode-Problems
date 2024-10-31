from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = sorted(nums1 + nums2)
        n = len(c)
        if n % 2 == 1:
            return c[n // 2]
        else:
            return (c[n // 2 - 1] + c[n // 2]) / 2.0




solution = Solution()

result = solution.findMedianSortedArrays([1,3],[2])

print("Resultado: ",result)