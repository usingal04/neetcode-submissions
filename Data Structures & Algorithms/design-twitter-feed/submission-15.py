class Twitter:

    def __init__(self):
        self.cnt = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.cnt, tweetId])
        self.cnt -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res, heap = [], []
        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId])-1
                cnt, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [cnt, tweetId, followeeId, index-1])
        
        while len(res) < 10 and heap:
            cnt, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                cnt, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, [cnt, tweetId, followeeId, index-1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
