class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        elements = []
        l, r = 0, 0
        L, R = len(word1), len(word2)
        word = 1

        while l < L and r < R:
            if word == 1:
                elements.append(word1[l])
                l += 1
                word = 2
            if word == 2:
                elements.append(word2[r])
                r += 1
                word = 1
        
        while l < L:
            elements.append(word1[l])
            l += 1
        
        while r < R:
            elements.append(word2[r])
            r += 1
        
        return ''.join(elements)