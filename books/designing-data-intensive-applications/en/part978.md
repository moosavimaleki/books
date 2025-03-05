
A stream-table join is actually very similar to a stream-stream join; the biggest difference is that
for the table changelog stream, the join uses a window that reaches back to the “beginning of time”
(a conceptually infinite window), with newer versions of records overwriting older ones. For the
stream input, the join might not maintain a window at all. ### Table-table join (materialized view maintenance) 
Consider the Twitter timeline example that we discussed in [“Describing Load”](ch01.html#sec_introduction_scalability_load). We
said that when a user wants to view their home timeline, it is too expensive to iterate over all the
people the user is following, find their recent tweets, and merge them. Instead, we want a timeline cache: a kind of per-user “inbox” to which tweets are written as they
are sent, so that reading the timeline is a single lookup. Materializing and maintaining this cache
requires the following event processing: *  When user u sends a new tweet, it is added to the timeline of every user who is following u.