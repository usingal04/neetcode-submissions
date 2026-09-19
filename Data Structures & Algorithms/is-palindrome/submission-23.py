class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        elements = []

        for char in s:
            if char.isalnum():
                elements.append(char.lower())
        
        l, r = 0, len(elements)-1

        while l <= r:
            if elements[l] != elements[r]:
                return False
            l += 1
            r -= 1
        
        return True