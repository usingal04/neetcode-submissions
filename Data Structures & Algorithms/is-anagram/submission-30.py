class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ss = {}
        tt = {}

        for char in s:
            if char in ss:
                ss[char] += 1
            else:
                ss[char] = 1
        
        for char in t:
            if char in tt:
                tt[char] += 1
            else:
                tt[char] = 1
        
        return ss == tt