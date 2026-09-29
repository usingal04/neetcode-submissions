"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return
        
        h = {}
        curr = head

        while curr:
            node = Node(curr.val)
            h[curr] = node
            curr = curr.next
        
        curr = head

        while curr:
            new_node = h[curr]
            new_node.next = h[curr.next] if curr.next else None
            new_node.random = h[curr.random] if curr.random else None
            curr = curr.next
        
        return h[head]