# https://leetcode.com/problems/design-twitter/

from __future__ import annotations

from collections import defaultdict
from functools import reduce
import heapq


class Tweet:
    def __init__(self: Tweet, tweet_id: int, timestamp: int) -> None:
        self.tweet_id = tweet_id
        self.timestamp = timestamp


class User:
    def __init__(
        self: User,
        user_id: int,
        tweets: set[Tweet] = None,
        follower_ids: set[int] = None,
        following_ids: set[int] = None,
    ) -> None:
        self.user_id = user_id
        self.tweets = tweets if tweets is not None else set()
        self.follower_ids = follower_ids if follower_ids is not None else set()
        self.following_ids = following_ids if following_ids is not None else set()

    def add_follower(self: User, follower_id: int) -> None:
        self.follower_ids.add(follower_id)

    def remove_follower(self: User, follower_id: int) -> None:
        self.follower_ids.remove(follower_id)

    def add_following(self: User, following_id: int) -> None:
        self.following_ids.add(following_id)

    def remove_following(self: User, following_id: int) -> None:
        self.following_ids.remove(following_id)

    def tweet(self: User, tweet_id: int, tweet_timestamp: int) -> None:
        self.tweets.add(Tweet(tweet_id, tweet_timestamp))


class Twitter:
    def __init__(self: Twitter) -> None:
        self.users = self.DefaultUserDict()
        self.timestamp = 0

    class DefaultUserDict(defaultdict):
        def __missing__(self, key) -> User:
            self[key] = User(key)
            return self[key]

    def postTweet(self: Twitter, userId: int, tweetId: int) -> None:
        self.users[userId].tweet(tweetId, self.timestamp)
        self.timestamp += 1

    def getNewsFeed(self: Twitter, userId: int) -> list[int]:
        return [
            tweet.tweet_id
            for tweet in heapq.nlargest(
                10,
                reduce(
                    lambda x, y: x | y,
                    [
                        self.users[follower_id].tweets
                        for follower_id in [
                            userId,
                            *list(self.users[userId].following_ids),
                        ]
                    ],
                ),
                key=lambda tweet: tweet.timestamp,
            )
        ]

    def follow(self: Twitter, followerId: int, followeeId: int) -> None:
        self.users[followeeId].add_follower(followerId)
        self.users[followerId].add_following(followeeId)

    def unfollow(self: Twitter, followerId: int, followeeId: int) -> None:
        try:
            self.users[followeeId].remove_follower(followerId)
            self.users[followerId].remove_following(followeeId)
        except:
            pass


t = Twitter()
t.postTweet(1, 5)
t.getNewsFeed(1)
t.follow(1, 2)
t.postTweet(2, 6)
print(t.getNewsFeed(1))
t.unfollow(1, 2)
t.getNewsFeed(1)
