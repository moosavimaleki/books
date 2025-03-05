
While this procedure ensures linearizable writes, it doesn’t guarantee linearizable reads—if you
read from a store that is asynchronously updated from the log, it may be stale. (To be precise, the
procedure described here provides sequential consistency
[[47](ch09.html#Attiya1994gw),
[64](ch09.html#Lamport1979ky)],
sometimes also known as timeline consistency
[[65](ch09.html#Soztutar2015vj),
[66](ch09.html#Cooper2008fn)],
a slightly weaker guarantee than linearizability.) To make reads linearizable, there are a few
options: *  
You can sequence reads through the log by appending a message, reading the log, and performing the
actual read when the message is delivered back to you. The message’s position in the log thus
defines the point in time at which the read happens. (Quorum reads in etcd work somewhat like this
[[16](ch09.html#Etcd)].) *  
If the log allows you to fetch the position of the latest log message in a linearizable way, you
can query that position, wait for all entries up to that position to be delivered to you, and then
perform the read. (This is the idea behind ZooKeeper’s sync() operation
[[15](ch09.html#Junqueira2013wi_ch9)].)