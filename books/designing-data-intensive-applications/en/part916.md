
Within each partition, the broker assigns a monotonically increasing sequence number, or offset,
to every message (in [Figure 11-3](#fig_stream_kafka_partitions), the numbers in boxes are message offsets).
Such a sequence number makes sense because a partition is append-only, so the messages within a
partition are totally ordered. There is no ordering guarantee across different partitions. ![ddia 1103](assets/ddia_1103.png) ###### Figure 11-3. Producers send messages by appending them to a topic-partition file, and consumers read these files sequentially. 
Apache Kafka
[[17](ch11.html#Kafka2015),
[18](ch11.html#Kreps2011wl)], Amazon Kinesis Streams
[[19](ch11.html#Kinesis2016)], and Twitter’s
DistributedLog [[20](ch11.html#Stewart2015vb),
[21](ch11.html#DistributedLog)] are log-based message
brokers that work like this. Google Cloud Pub/Sub is architecturally similar but exposes a
JMS-style API rather than a log abstraction [[16](ch11.html#GooglePubSub)].
Even though these message brokers write all messages to disk, they are able to achieve throughput of
millions of messages per second by partitioning across multiple machines, and fault tolerance by
replicating messages [[22](ch11.html#Kreps2014wz), [23](ch11.html#Paramasivam2015um)]. ### Logs compared to traditional messaging