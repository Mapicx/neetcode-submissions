import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        self.followMap[userId].add(userId)
        heap = []

        for followeeId in self.followMap[userId]:
            if self.tweetMap[followeeId]:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]

                heapq.heappush(
                    heap,
                    [count, tweetId, followeeId, index]
                )

        while heap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(heap)

            res.append(tweetId)

            index -= 1

            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]

                heapq.heappush(
                    heap,
                    [count, tweetId, followeeId, index]
                )

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)