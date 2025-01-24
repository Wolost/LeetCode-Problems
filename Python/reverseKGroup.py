from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def has_k_nodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k
        
        def reverse_k_nodes(start, k):
            prev, current = None, start
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev, current
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while has_k_nodes(prev_group_end.next, k):
            start = prev_group_end.next
            end, next_group_start = reverse_k_nodes(start, k)
            
            prev_group_end.next = end
            start.next = next_group_start
            
            prev_group_end = start
        
        return dummy.next

solution = Solution()

result = solution.reverseKGroup([1,2,3,4])

print("Resultado: ",result)