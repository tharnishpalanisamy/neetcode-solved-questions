class Twitter:

    def __init__(self):
        self.tweets = {} 
        self.followers = {} 
        self.time = 0 

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets :
            self.tweets[userId] = [] 
        self.tweets[userId].append((self.time , tweetId))
        self.time -= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
            res= [] 
            maxHeap = [] 

            if userId not in self.followers :
                self.followers[userId] = set()
            self.followers[userId].add(userId) 

            for follower in self.followers[userId] :
                if follower in self.tweets :
                    index = len(self.tweets[follower]) -1 
                    time , tweetId = self.tweets[follower][index] 
                    maxHeap.append([time,tweetId,follower,index-1])  
            heapq.heapify(maxHeap)
            while maxHeap and len(res) < 10 :
                time,tweetId,follower,index = heapq.heappop(maxHeap) 
                res.append(tweetId) 
                if index >= 0 :
                    time , tweet = self.tweets[follower][index]
                    heapq.heappush(maxHeap,[time,tweet,follower,index-1])
            return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers :
            self.followers[followerId] = set() 
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None: 
        if followerId in self.followers and followeeId in self.followers[followerId] :
            self.followers[followerId].remove(followeeId)
        
