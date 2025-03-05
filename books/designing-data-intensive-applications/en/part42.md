SELECT tweets.*, users.* FROM tweets
  JOIN users   ON tweets.sender_id    = users.id
  JOIN follows ON follows.followee_id = users.id
  WHERE follows.follower_id = current_user 2.  Maintain a cache for each user’s home timeline—like a mailbox of tweets for each recipient
user (see [Figure 1-3](#fig_twitter_timelines)). When a user posts a tweet, look up all the people who
follow that user, and insert the new tweet into each of their home timeline caches. The request to
read the home timeline is then cheap, because its result has been computed ahead of time. ![ddia 0102](assets/ddia_0102.png) ###### Figure 1-2. Simple relational schema for implementing a Twitter home timeline. ![ddia 0103](assets/ddia_0103.png) ###### Figure 1-3. Twitter’s data pipeline for delivering tweets to followers, with load parameters as of November 2012 [[16](ch01.html#Krikorian2012)]. The first version of Twitter used approach 1, but the systems struggled to keep up with the load of
home timeline queries, so the company switched to approach 2. This works better because the average
rate of published tweets is almost two orders of magnitude lower than the rate of home timeline
reads, and so in this case it’s preferable to do more work at write time and less at read time.