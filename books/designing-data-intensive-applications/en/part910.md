*  When querying a database, the result is typically based on a point-in-time snapshot of the data;
if another client subsequently writes something to the database that changes the query result, the
first client does not find out that its prior result is now outdated (unless it repeats the query,
or polls for changes). By contrast, message brokers do not support arbitrary queries, but they do
notify clients when data changes (i.e., when new messages become available). 
This is the traditional view of message brokers, which is encapsulated in standards like JMS
[[14](ch11.html#Hapner2013uk)] and AMQP
[[15](ch11.html#Aiyagari2008th)] and implemented in software
like RabbitMQ, ActiveMQ, HornetQ, Qpid, TIBCO Enterprise Message Service, IBM MQ, Azure Service
Bus, and Google Cloud Pub/Sub
[[16](ch11.html#GooglePubSub)]. ### Multiple consumers 
When multiple consumers read messages in the same topic, two main patterns of messaging are
used, as illustrated in [Figure 11-1](#fig_stream_multi_consumer): Load balancing 
Each message is delivered to one of the consumers, so the consumers can share the work of
processing the messages in the topic. The broker may assign messages to consumers arbitrarily.
This pattern is useful when the messages are expensive to process, and so you want to be able to
add consumers to parallelize the processing. (In AMQP, you can implement load balancing by having
multiple clients consuming from the same queue, and in JMS it is called a shared subscription.)