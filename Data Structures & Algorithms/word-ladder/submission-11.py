class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        d = defaultdict(list)

        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + '*' + w[j+1:]
                d[pattern].append(w)

        res = 1
        q = deque([beginWord])
        seen = set([beginWord])

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res

                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:] 
                    for nei_word in d[pattern]:
                        if nei_word not in seen:
                            seen.add(nei_word) 
                            q.append(nei_word)

            res += 1

        return 0      