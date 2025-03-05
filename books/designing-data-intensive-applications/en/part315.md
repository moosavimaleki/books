
How does leader-based replication work under the hood? Several different replication methods are
used in practice, so let’s look at each one briefly. ### Statement-based replication 
In the simplest case, the leader logs every write request (statement) that it executes and sends
that statement log to its followers. For a relational database, this means that every INSERT,
UPDATE, or DELETE statement is forwarded to followers, and each follower parses and executes
that SQL statement as if it had been received from a client. Although this may sound reasonable, there are various ways in which this approach to replication can
break down: *  Any statement that calls a nondeterministic function, such as NOW() to get the current date
and time or RAND() to get a random number, is likely to generate a different value on each
replica. *  If statements use an autoincrementing column, or if they depend on the existing data in the
database (e.g., UPDATE … WHERE ), they must be executed in exactly the same
order on each replica, or else they may have a different effect. This can be limiting when there
are multiple concurrently executing transactions.