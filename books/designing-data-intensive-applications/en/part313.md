*  
Discarding writes is especially dangerous if other storage systems outside of the database need to
be coordinated with the database contents.

For example, in one incident at GitHub [[13](ch05.html#Newland2012tw)], an out-of-date MySQL follower
was promoted to leader. The database used an autoincrementing counter to assign primary keys to
new rows, but because the new leader’s counter lagged behind the old leader’s, it reused some
primary keys that were previously assigned by the old leader. These primary keys were also used in
a Redis store, so the reuse of primary keys resulted in inconsistency between MySQL and Redis,
which caused some private data to be disclosed to the wrong users. *  
In certain fault scenarios (see [Chapter 8](ch08.html#ch_distributed)), it could happen that two nodes both believe
that they are the leader. This situation is called split brain, and it is dangerous: if both
leaders accept writes, and there is no process for resolving conflicts (see
[“Multi-Leader Replication”](#sec_replication_multi_leader)), data is likely to be lost or corrupted. As a safety catch, some
systems have a mechanism to shut down one node if two leaders are
detected.[ii](ch05.html#idm140605776275968)
However, if this mechanism is not carefully designed, you can end up with both nodes being shut down
[[14](ch05.html#Imbriaco2012tx_ch5)].