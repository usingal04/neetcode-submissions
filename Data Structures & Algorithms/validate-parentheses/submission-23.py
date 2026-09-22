class Solution:
    def isValid(self, s: str) -> bool:
        
        h = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }

        stk = []

        for bracket in s:
            if bracket not in h:
                stk.append(bracket)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != h[bracket]:
                        return False
        
        return not stk
