If you have multiple web servers handling user requests, the activity events for a particular user
are most likely scattered across various different servers’ log files. You can implement
sessionization by using a session cookie, user ID, or similar identifier as the grouping key and
bringing all the activity events for a particular user together in one place, while distributing
different users’ events across different partitions. ### Handling skew 
The pattern of “bringing all records with the same key to the same place” breaks down if there is a
very large amount of data related to a single key. For example, in a social network, most users
might be connected to a few hundred people, but a small number of celebrities may have many
millions of followers. Such disproportionately active database records are known as linchpin objects
[[38](ch10.html#Ajoux2015wh_ch10)] or hot keys. Collecting all activity related to a celebrity (e.g., replies to something they posted) in a single
reducer can lead to significant skew (also known as hot spots)—that is, one
reducer that must process significantly more records than the others (see
[“Skewed Workloads and Relieving Hot Spots”](ch06.html#sec_partitioning_skew)). Since a MapReduce job is only complete when all of its mappers and
reducers have completed, any subsequent jobs must wait for the slowest reducer to complete before
they can start.