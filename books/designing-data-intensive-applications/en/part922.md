Even if a consumer does fall too far behind and starts missing messages, only that consumer is
affected; it does not disrupt the service for other consumers. This fact is a big operational
advantage: you can experimentally consume a production log for development, testing, or debugging
purposes, without having to worry much about disrupting production services. When a consumer is shut
down or crashes, it stops consuming resources—the only thing that remains is its consumer offset. This behavior also contrasts with traditional message brokers, where you need to be careful to delete
any queues whose consumers have been shut down—otherwise they continue unnecessarily accumulating
messages and taking away memory from consumers that are still active. ### Replaying old messages 
We noted previously that with AMQP- and JMS-style message brokers, processing and acknowledging
messages is a destructive operation, since it causes the messages to be deleted on the broker. On
the other hand, in a log-based message broker, consuming messages is more like reading from a file:
it is a read-only operation that does not change the log.