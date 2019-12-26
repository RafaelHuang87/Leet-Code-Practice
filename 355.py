class User(object):
    """
    User structure
    """

    def __init__(self, userId):
        self.userid = userId
        self.tweets = set()
        self.following = set()


class Tweet(object):
    """
    Tweet structure
    """

    def __init__(self, tweetId, userId, ts):
        self.tweetid = tweetId
        self.userid = userId
        self.ts = ts

    def __cmp__(self, other):
        # call global(builtin) function cmp for int
        if other.ts < self.ts:
            return -1
        elif other.ts == self.ts:
            return 0
        else:
            return 1
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = 0
        self.usermap = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.usermap:
            self.usermap[userId] = User(userId)
        tweet = Tweet(tweetId, userId, self.tweets)
        self.usermap[userId].tweets.add(tweet)
        self.tweets += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        import heapq
        res, que = list(), []
        if userId not in self.usermap:
            return res
        mainUser = self.usermap[userId]
        for t in mainUser.tweets:
            heapq.heappush(que, t)
        for u in mainUser.following:
            for t in u.tweets:
                heapq.heappush(que, t)
        n = 0
        while que and n < 10:
            res.append(heapq.heappop(que).tweetid)
            n += 1
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId not in self.usermap:
            self.usermap[followeeId] = User(followeeId)
        if followerId not in self.usermap:
            self.usermap[followerId] = User(followerId)
        if followerId == followeeId:
            return
        followee = self.usermap[followeeId]
        self.usermap[followerId].following.add(followee)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if (followerId == followeeId) or (followerId not in self.usermap) or (followeeId not in self.usermap):
            return
        followee = self.usermap[followeeId]
        if followee in self.usermap.get(followerId).following:
            self.usermap.get(followerId).following.remove(followee)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)