
For that reason, it is impractical for all followers to be synchronous: any one node outage would
cause the whole system to grind to a halt. In practice, if you enable synchronous replication on a
database, it usually means that one of the followers is synchronous, and the others are
asynchronous. If the synchronous follower becomes unavailable or slow, one of the asynchronous
followers is made synchronous. This guarantees that you have an up-to-date copy of the data on at
least two nodes: the leader and one synchronous follower. This configuration is sometimes also
called semi-synchronous [[7](ch05.html#Matsunobu2014wu)]. Often, leader-based replication is configured to be completely asynchronous. In this case, if the
leader fails and is not recoverable, any writes that have not yet been replicated to followers are
lost. This means that a write is not guaranteed to be durable, even if it has been confirmed to the
client. However, a fully asynchronous configuration has the advantage that the leader can continue
processing writes, even if all of its followers have fallen behind.