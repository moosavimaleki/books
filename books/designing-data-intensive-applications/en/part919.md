
This offset is in fact very similar to the log sequence number that is commonly found in
single-leader database replication, and which we discussed in [“Setting Up New Followers”](ch05.html#sec_replication_new_replica). In
database replication, the log sequence number allows a follower to reconnect to a leader after it
has become disconnected, and resume replication without skipping any writes. Exactly the same
principle is used here: the message broker behaves like a leader database, and the consumer like a
follower. 
If a consumer node fails, another node in the consumer group is assigned the failed consumer’s
partitions, and it starts consuming messages at the last recorded offset. If the consumer had
processed subsequent messages but not yet recorded their offset, those messages will be processed a
second time upon restart. We will discuss ways of dealing with this issue later in the chapter. ### Disk space usage 
If you only ever append to the log, you will eventually run out of disk space. To reclaim disk
space, the log is actually divided into segments, and from time to time old segments are deleted or
moved to archive storage. (We’ll discuss a more sophisticated way of freeing disk space later.)