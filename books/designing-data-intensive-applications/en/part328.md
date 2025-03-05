This can happen if a user makes several reads from different replicas. For example,
[Figure 5-4](#fig_replication_monotonic_reads) shows user 2345 making the same query twice, first to a follower
with little lag, then to a follower with greater lag. (This scenario is quite likely if the user
refreshes a web page, and each request is routed to a random server.) The first query returns a
comment that was recently added by user 1234, but the second query doesn’t return anything because
the lagging follower has not yet picked up that write. In effect, the second query is observing the
system at an earlier point in time than the first query. This wouldn’t be so bad if the first query
hadn’t returned anything, because user 2345 probably wouldn’t know that user 1234 had recently added
a comment. However, it’s very confusing for user 2345 if they first see user 1234’s comment appear,
and then see it disappear again.