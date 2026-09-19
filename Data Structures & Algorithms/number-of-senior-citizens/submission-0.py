class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        num_seniors = 0

        for detail in details:
            age = int(detail[-4:-2])
            if age > 60:
                num_seniors += 1
        
        return num_seniors