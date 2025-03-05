
The log-based approach trivially supports fan-out messaging, because several consumers can
independently read the log without affecting each other—reading a message does not delete it from
the log. To achieve load balancing across a group of consumers, instead of assigning individual
messages to consumer clients, the broker can assign entire partitions to nodes in the consumer
group. 
Each client then consumes all the messages in the partitions it has been assigned. Typically, when
a consumer has been assigned a log partition, it reads the messages in the partition sequentially,
in a straightforward single-threaded manner. This coarse-grained load balancing approach has some
downsides: *  The number of nodes sharing the work of consuming a topic can be at most the number of log
partitions in that topic, because messages within the same partition are delivered to the same
node.[i](ch11.html#idm140605757123312) *  If a single message is slow to process, it holds up the processing of subsequent messages in that
partition (a form of head-of-line blocking; see [“Describing Performance”](ch01.html#sec_introduction_percentiles)).