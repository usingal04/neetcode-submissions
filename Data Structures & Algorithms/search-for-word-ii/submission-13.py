class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        d = TrieNode()

        for w in words:
            d.addWord(w)
        
        res, seen = set(), set()

        def backtrack(i, j, node, word):
            if i < 0 or i == m or j < 0 or j == n or (i, j) in seen or board[i][j] not in node.children:
                return
            
            seen.add((i, j))
            node = node.children[board[i][j]]
            word += board[i][j]

            if node.isWord:
                res.add(word)
            
            backtrack(i+1, j, node, word)
            backtrack(i, j+1, node, word)
            backtrack(i-1, j, node, word)
            backtrack(i, j-1, node, word)
        
            seen.remove((i, j))
        
        for i in range(m):
            for j in range(n):
                backtrack(i, j, d, '')
        
        return list(res)