class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in h:
                h[key].append(s)
            else:
                h[key] = [s]
        
        return [val for val in h.values()]