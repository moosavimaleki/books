The join of the streams corresponds directly to the join of the tables in that query. The timelines
are effectively a cache of the result of this query, updated every time the underlying tables
change.[iii](ch11.html#idm140605756368864) ### Time-dependence of joins 
The three types of joins described here (stream-stream, stream-table, and table-table) have a lot in
common: they all require the stream processor to maintain some state (search and click events, user
profiles, or follower list) based on one join input, and query that state on messages from the other
join input. The order of the events that maintain the state is important (it matters whether you first follow
and then unfollow, or the other way round). In a partitioned log, the ordering of events within a
single partition is preserved, but there is typically no ordering guarantee across different streams
or partitions. This raises a question: if events on different streams happen around a similar time, in which order
are they processed? In the stream-table join example, if a user updates their profile, which
activity events are joined with the old profile (processed before the profile update), and which are
joined with the new profile (processed after the profile update)? Put another way: if state changes
over time, and you join with some state, what point in time do you use for the join
[[45](ch11.html#Jagadish1995ee)]?