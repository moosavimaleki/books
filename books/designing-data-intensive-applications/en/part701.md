An important aspect of total order broadcast is that the order is fixed at the time the messages are
delivered: a node is not allowed to retroactively insert a message into an earlier position in the
order if subsequent messages have already been delivered. This fact makes total order broadcast
stronger than timestamp ordering. 
Another way of looking at total order broadcast is that it is a way of creating a log (as in a
replication log, transaction log, or write-ahead log): delivering a message is like appending to the
log. Since all nodes must deliver the same messages in the same order, all nodes can read the log
and see the same sequence of messages. 
Total order broadcast is also useful for implementing a lock service that provides fencing tokens
(see [“Fencing tokens”](ch08.html#sec_distributed_fencing_tokens)). Every request to acquire the lock is appended as a message
to the log, and all messages are sequentially numbered in the order they appear in the log. The
sequence number can then serve as a fencing token, because it is monotonically increasing. In
ZooKeeper, this sequence number is called zxid
[[15](ch09.html#Junqueira2013wi_ch9)].