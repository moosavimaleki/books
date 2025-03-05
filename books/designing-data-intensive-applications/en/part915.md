Why can we not have a hybrid, combining the durable storage approach of databases with the
low-latency notification facilities of messaging? This is the idea behind log-based message
brokers. ### Using logs for message storage 
A log is simply an append-only sequence of records on disk. We previously discussed logs in the
context of log-structured storage engines and write-ahead logs in [Chapter 3](ch03.html#ch_storage), and in the context
of replication in [Chapter 5](ch05.html#ch_replication). 
The same structure can be used to implement a message broker: a producer sends a message by
appending it to the end of the log, and a consumer receives messages by reading the log
sequentially. If a consumer reaches the end of the log, it waits for a notification that a new
message has been appended. The Unix tool tail -f, which watches a file for data being appended,
essentially works like this. In order to scale to higher throughput than a single disk can offer, the log can be partitioned
(in the sense of [Chapter 6](ch06.html#ch_partitioning)). Different partitions can then be hosted on different
machines, making each partition a separate log that can be read and written independently from other
partitions. A topic can then be defined as a group of partitions that all carry messages of the same
type. This approach is illustrated in [Figure 11-3](#fig_stream_kafka_partitions).