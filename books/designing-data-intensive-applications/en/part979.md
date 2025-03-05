*  When a user deletes a tweet, it is removed from all users’ timelines. *  When user u1 starts following user u2, recent tweets by u2 are added to
u1’s timeline. *  When user u1 unfollows user u2, tweets by u2 are removed from u1’s
timeline. To implement this cache maintenance in a stream processor, you need streams of events for tweets
(sending and deleting) and for follow relationships (following and unfollowing). The stream process
needs to maintain a database containing the set of followers for each user so that it knows which
timelines need to be updated when a new tweet arrives
[[86](ch11.html#SamzaNewsfeed)]. 
Another way of looking at this stream process is that it maintains a materialized view for a query
that joins two tables (tweets and follows), something like the following: ```
`SELECT` `follows``.``follower_id` `AS` `timeline_id``,`
  `array_agg``(``tweets``.``*` `ORDER` `BY` `tweets``.``timestamp` `DESC``)`
`FROM` `tweets`
`JOIN` `follows` `ON` `follows``.``followee_id` `=` `tweets``.``sender_id`
`GROUP` `BY` `follows``.``follower_id`
```