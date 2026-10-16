"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return 
        
        h = {}
        start = node
        stk = [start]
        seen = set([start])

        while stk:
            node = stk.pop()
            h[node] = Node(node.val)

            for nei in node.neighbors:
                if nei not in seen:
                    seen.add(nei)
                    stk.append(nei)
        
        for old_node, new_node in h.items():
            for old_nei in old_node.neighbors:
                new_nei = h[old_nei]
                new_node.neighbors.append(new_nei)
        
        return h[start]