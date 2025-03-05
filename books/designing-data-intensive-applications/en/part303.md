3.  When a client wants to read from the database, it can query either the leader or any of the
followers. However, writes are only accepted on the leader (the followers are read-only from the
client’s point of view). ![ddia 0501](assets/ddia_0501.png) ###### Figure 5-1. Leader-based (master–slave) replication. 
This mode of replication is a built-in feature of many relational databases, such as PostgreSQL
(since version 9.0), MySQL, Oracle Data Guard
[[2](ch05.html#Oracle2013uz)],
and SQL Server’s AlwaysOn Availability Groups
[[3](ch05.html#AlwaysOn2012)].
It is also used in some nonrelational databases, including MongoDB, RethinkDB, and Espresso
[[4](ch05.html#Qiao2013uv_ch5)]. Finally, leader-based
replication is not restricted to only databases: distributed message brokers such as Kafka
[[5](ch05.html#Rao2013tf)]
and RabbitMQ highly available queues
[[6](ch05.html#RabbitMQ2013)]
also use it. Some network filesystems and replicated block devices such as DRBD are similar. ## Synchronous Versus Asynchronous Replication 
An important detail of a replicated system is whether the replication happens synchronously or
asynchronously. (In relational databases, this is often a configurable option; other systems are
often hardcoded to be either one or the other.)