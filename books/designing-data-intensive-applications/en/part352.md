
Some data storage systems take a different approach, abandoning the concept of a leader and
allowing any replica to directly accept writes from clients. Some of the earliest replicated data
systems were leaderless [[1](ch05.html#Lindsay1979wv_ch5),
[44](ch05.html#Gifford1979if)], but the
idea was mostly forgotten during the era of dominance of relational databases. It once again became
a fashionable architecture for databases after Amazon used it for its in-house Dynamo system
[[37](ch05.html#DeCandia2007ui_ch5)].[vi](ch05.html#idm140605775804016)
Riak, Cassandra, and Voldemort are open source datastores with leaderless replication models inspired
by Dynamo, so this kind of database is also known as Dynamo-style. In some leaderless implementations, the client directly sends its writes to several replicas, while
in others, a coordinator node does this on behalf of the client. However, unlike a leader database,
that coordinator does not enforce a particular ordering of writes. As we shall see, this difference in design has
profound consequences for the way the database is used.