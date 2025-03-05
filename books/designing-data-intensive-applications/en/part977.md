
To perform this join, the stream process needs to look at one activity event at a time, look up the
event’s user ID in the database, and add the profile information to the activity event. The database
lookup could be implemented by querying a remote database; however, as discussed in
[“Example: analysis of user activity events”](ch10.html#sec_batch_join_example), such remote queries are likely to be slow and risk overloading the database
[[75](ch11.html#Kreps2014wm_ch11)]. 
Another approach is to load a copy of the database into the stream processor so that it can be
queried locally without a network round-trip. This technique is very similar to the hash joins we
discussed in [“Map-Side Joins”](ch10.html#sec_batch_map_joins): the local copy of the database might be an in-memory hash
table if it is small enough, or an index on the local disk. 
The difference to batch jobs is that a batch job uses a point-in-time snapshot of the database as
input, whereas a stream processor is long-running, and the contents of the database are likely to
change over time, so the stream processor’s local copy of the database needs to be kept up to date.
This issue can be solved by change data capture: the stream processor can subscribe to a changelog
of the user profile database as well as the stream of activity events. When a profile is created or
modified, the stream processor updates its local copy. Thus, we obtain a join between two streams:
the activity events and the profile updates.