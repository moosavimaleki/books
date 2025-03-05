Fan-out 
Each message is delivered to all of the consumers. Fan-out allows several independent consumers
to each “tune in” to the same broadcast of messages, without affecting each other—the streaming
equivalent of having several different batch jobs that read the same input file. (This feature is
provided by topic subscriptions in JMS, and exchange bindings in AMQP.) ![ddia 1101](assets/ddia_1101.png) ###### Figure 11-1. (a) Load balancing: sharing the work of consuming a topic among consumers; (b) fan-out: delivering each message to multiple consumers. The two patterns can be combined: for example, two separate groups of consumers may each subscribe
to a topic, such that each group collectively receives all messages, but within each group only one
of the nodes receives each message. ### Acknowledgments and redelivery 
Consumers may crash at any time, so it could happen that a broker delivers a message to a consumer
but the consumer never processes it, or only partially processes it before crashing. In order to
ensure that the message is not lost, message brokers use acknowledgments: a client must
explicitly tell the broker when it has finished processing a message so that the broker can remove
it from the queue.