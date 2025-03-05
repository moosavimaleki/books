
To make this idea more concrete, let’s consider Twitter as an example, using data published in
November 2012 [[16](ch01.html#Krikorian2012)].
Two of Twitter’s main operations are: Post tweet A user can publish a new message to their followers (4.6k requests/sec on average, over
12k requests/sec at peak). Home timeline A user can view tweets posted by the people they follow (300k requests/sec). 
Simply handling 12,000 writes per second (the peak rate for posting tweets) would be fairly easy.
However, Twitter’s scaling challenge is not primarily due to tweet volume, but due to
fan-out[ii](ch01.html#idm140605786070912)—each user follows many people, and each user
is followed by many people. There are broadly two ways of implementing these two operations: 1.  Posting a tweet simply inserts the new tweet into a global collection of tweets. When a user
requests their home timeline, look up all the people they follow, find all the tweets for each of
those users, and merge them (sorted by time). In a relational database like in
[Figure 1-2](#fig_twitter_relational), you could write a query such as: