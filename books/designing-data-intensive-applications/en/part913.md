![ddia 1102](assets/ddia_1102.png) ###### Figure 11-2. Consumer 2 crashes while processing m3, so it is redelivered to consumer 1 at a later time. 
Even if the message broker otherwise tries to preserve the order of messages (as required by both
the JMS and AMQP standards), the combination of load balancing with redelivery inevitably leads to
messages being reordered. To avoid this issue, you can use a separate queue per consumer (i.e., not
use the load balancing feature). Message reordering is not a problem if messages are completely
independent of each other, but it can be important if there are causal dependencies between
messages, as we shall see later in the chapter. ## Partitioned Logs 
Sending a packet over a network or making a request to a network service is normally a transient
operation that leaves no permanent trace. Although it is possible to record it permanently (using
packet capture and logging), we normally don’t think of it that way. Even message brokers that
durably write messages to disk quickly delete them again after they have been delivered to
consumers, because they are built around a transient messaging mindset.