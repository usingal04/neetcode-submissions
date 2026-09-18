class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        minLen = float('inf')

        for s in strs:
            if len(s) < minLen:
                minLen = len(s)
        
        index = 0

        while index < minLen:
            for s in strs:
                if s[index] != strs[0][index]:
                    return s[:index]
            index += 1
        
        return strs[0][:index]