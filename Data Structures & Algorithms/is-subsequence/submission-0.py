class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s == "":
            return True
        
        S, T = len(s), len(t)

        if S > T:
            return False
        
        j = 0

        for i in range(T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j += 1
        
        return False