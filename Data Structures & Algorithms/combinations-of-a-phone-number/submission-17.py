class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        h = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz' 
        }

        if digits == "":
            return []

        res, sol = [], []

        def backtrack(i):
            if len(sol) == len(digits):
                res.append(''.join(sol))
                return
            
            for letter in h[digits[i]]:
                sol.append(letter)
                backtrack(i+1)
                sol.pop()
        
        backtrack(0)
        return res