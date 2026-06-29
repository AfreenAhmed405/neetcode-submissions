import heapq
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        # Global timestamp to track the chronological order of tweets
        self.timestamp = 0
        # Maps userId -> list of pairs: [timestamp, tweetId]
        self.tweetMap = defaultdict(list)
        # Maps userId -> set of followeeIds
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Decrement timestamp because Python's heapq is a min-heap by default.
        # Negative values allow us to pop the smallest value (which represents the latest tweet).
        self.tweetMap[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        # Ensure a user always sees their own tweets
        self.followMap[userId].add(userId)

        # For every person the user follows, get their latest tweet
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                time, tweetId = self.tweetMap[followeeId][index]
                # Store: time, tweetId, followeeId, and index of the next available tweet
                maxHeap.append([time, tweetId, followeeId, index - 1])

        # Convert the array into a valid heap structure
        heapq.heapify(maxHeap)

        # Retrieve up to 10 most recent tweets
        while maxHeap and len(res) < 10:
            time, tweetId, followeeId, next_idx = heapq.heappop(maxHeap)
            res.append(tweetId)
            
            # If the user has more older tweets left, push the next one into the heap
            if next_idx >= 0:
                next_time, next_tweetId = self.tweetMap[followeeId][next_idx]
                heapq.heappush(maxHeap, [next_time, next_tweetId, followeeId, next_idx - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Avoid removing the user from their own follow map if they try to unfollow themselves
        if followeeId in self.followMap[followerId] and followerId != followeeId:
            self.followMap[followerId].remove(followeeId)