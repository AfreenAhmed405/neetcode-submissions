import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                maxHeap.append([time, tweetId, followeeId, index - 1])

        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            time, tweetId, followeeId, next_idx = heapq.heappop(maxHeap)
            res.append(tweetId)
            
            if next_idx >= 0:
                next_time, next_tweetId = self.tweetMap[followeeId][next_idx]
                heapq.heappush(maxHeap, [next_time, next_tweetId, followeeId, next_idx - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId] and followerId != followeeId:
            self.followMap[followerId].remove(followeeId)