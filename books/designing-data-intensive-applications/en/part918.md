Thus, in situations where messages may be expensive to process and you want to parallelize
processing on a message-by-message basis, and where message ordering is not so important, the
JMS/AMQP style of message broker is preferable. On the other hand, in situations with high message
throughput, where each message is fast to process and where message ordering is important, the
log-based approach works very well. ### Consumer offsets 
Consuming a partition sequentially makes it easy to tell which messages have been processed: all
messages with an offset less than a consumer’s current offset have already been processed, and all
messages with a greater offset have not yet been seen. Thus, the broker does not need to track
acknowledgments for every single message—it only needs to periodically record the consumer
offsets. The reduced bookkeeping overhead and the opportunities for batching and pipelining in this
approach help increase the throughput of log-based systems.