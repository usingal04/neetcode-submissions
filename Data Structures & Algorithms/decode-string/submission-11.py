class Solution:
    def decodeString(self, s: str) -> str:
        
        stk = []

        for char in s:
            if char != ']':
                stk.append(char)
            else:
                curr = ''
                while stk and stk[-1] != '[':
                    curr = stk.pop() + curr
                stk.pop()
                num = ''
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                stk.append(int(num) * curr)
        
        return ''.join(stk)