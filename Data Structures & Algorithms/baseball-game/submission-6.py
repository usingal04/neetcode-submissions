class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stk = []

        for operation in operations:
            if operation == 'C':
                stk.pop()
            elif operation == '+':
                stk.append(stk[-1] + stk[-2])
            elif operation == 'D':
                stk.append(stk[-1] * 2)
            else:
                stk.append(int(operation))
        
        return sum(stk)