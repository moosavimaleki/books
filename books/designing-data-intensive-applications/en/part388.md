[iii](ch05.html#idm140605776151312-marker) The
term eventual consistency was coined by Douglas Terry et al.
[[24](ch05.html#Terry1994fp)], popularized by Werner Vogels
[[22](ch05.html#Vogels2008ey)], and became the battle cry of many NoSQL
projects. However, not only NoSQL databases are eventually consistent: followers in an
asynchronously replicated relational database have the same characteristics. [iv](ch05.html#idm140605776056032-marker) If the database is partitioned (see
[Chapter 6](ch06.html#ch_partitioning)), each partition has one leader. Different partitions
may have their leaders on different nodes, but each partition must nevertheless have one leader
node. [v](ch05.html#idm140605775851008-marker) Not to be confused with a
star schema (see [“Stars and Snowflakes: Schemas for Analytics”](ch03.html#sec_storage_analytics_schemas)), which
describes the structure of a data model, not the communication topology between nodes. [vi](ch05.html#idm140605775804016-marker) Dynamo
is not available to users outside of Amazon. Confusingly, AWS offers a hosted database product
called DynamoDB, which uses a completely different architecture: it is based on
single-leader replication. [vii](ch05.html#idm140605775762224-marker) Sometimes
this kind of quorum is called a strict quorum, to contrast with sloppy quorums
(discussed in [“Sloppy Quorums and Hinted Handoff”](#sec_replication_sloppy_quorum)).