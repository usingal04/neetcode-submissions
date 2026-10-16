class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        d = defaultdict(list)

        for u, v in prerequisites:
            d[u].append(v)
        
        unvisited = 0
        visiting = 1
        visited = 2

        states = [unvisited] * numCourses

        def dfs(node):
            state = states[node]

            if state == visited:
                return True
            
            if state == visiting:
                return False
            
            states[node] = visiting
            for nei in d[node]:
                if not dfs(nei):
                    return False
            
            states[node] = visited
            return True
    
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True