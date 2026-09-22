class Solution:
    def simplifyPath(self, path: str) -> str:
        
        paths = path.split('/')
        stk = []

        for p in paths:
            if p == '..':
                if stk:
                    stk.pop()
            elif p != '' and p != '.':
                    stk.append(p)
        
        return '/' + '/'.join(stk)