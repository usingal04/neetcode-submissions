# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        nodes = []

        for l in lists:
            curr = l
            while curr:
                nodes.append(curr.val)
                curr = curr.next
        
        heapq.heapify(nodes)

        dummy = ListNode()
        curr = dummy

        while nodes:
            curr.next = ListNode(heapq.heappop(nodes))
            curr = curr.next
        
        return dummy.next