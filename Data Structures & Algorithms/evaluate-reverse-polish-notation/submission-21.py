class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []

        for token in tokens:
            if token not in ['+', '-', '/', '*']:
                stk.append(token)
            else:
                operand2 = int(stk.pop())
                operand1 = int(stk.pop())

                if token == '+':
                    stk.append(operand1 + operand2)
                elif token == '-':
                    stk.append(operand1 - operand2)
                elif token == '/':
                    stk.append(operand1 / operand2)
                else:
                    stk.append(operand1 * operand2)
            
        return int(stk[0])