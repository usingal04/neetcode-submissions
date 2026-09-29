# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = l1
        cur2 = l2

        elements1 = []
        elements2 = []

        while cur1:
            elements1.append(str(cur1.val))
            cur1 = cur1.next
        
        while cur2:
            elements2.append(str(cur2.val))
            cur2 = cur2.next
        
        elements1.reverse()
        elements2.reverse()
        int1 = int(''.join(elements1))
        int2 = int(''.join(elements2))
        summ = reversed(str(int1+int2))

        dummy = ListNode()
        curr = dummy

        for node in summ:
            curr.next = ListNode(int(node))
            curr = curr.next
        
        return dummy.next