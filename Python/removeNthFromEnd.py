from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        result = ListNode(0,head)
        first = second = result
        
        for _ in range(n + 1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        
        return result.next
    
solution = Solution()

result = solution.removeNthFromEnd([1,2,3,4,5],2)

print("Resultado: ",result)