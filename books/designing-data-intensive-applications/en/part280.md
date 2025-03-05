### Message brokers 
In the past, the landscape of message brokers was dominated by commercial enterprise software from
companies such as TIBCO, IBM WebSphere, and webMethods. More recently, open source implementations
such as RabbitMQ, ActiveMQ, HornetQ, NATS, and Apache Kafka have become popular. We will compare them
in more detail in [Chapter 11](ch11.html#ch_stream). 
The detailed delivery semantics vary by implementation and configuration, but in general, message
brokers are used as follows: one process sends a message to a named queue or topic, and the
broker ensures that the message is delivered to one or more consumers of or subscribers to that
queue or topic. There can be many producers and many consumers on the same topic. A topic provides only one-way dataflow. However, a consumer may itself publish messages to another
topic (so you can chain them together, as we shall see in [Chapter 11](ch11.html#ch_stream)), or to a reply queue that
is consumed by the sender of the original message (allowing a request/response dataflow, similar to
RPC).