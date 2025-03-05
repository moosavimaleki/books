However, all of these trade-offs depend on the performance characteristics of the underlying
infrastructure: in some systems, network delay may be lower than disk access latency, and network
bandwidth may be comparable to disk bandwidth. There is no universally ideal trade-off for all
situations, and the merits of local versus remote state may also shift as storage and networking
technologies evolve. # Summary In this chapter we have discussed event streams, what purposes they serve, and how to process them.
In some ways, stream processing is very much like the batch processing we discussed in [Chapter 10](ch10.html#ch_batch),
but done continuously on unbounded (never-ending) streams rather than on a fixed-size input. From
this perspective, message brokers and event logs serve as the streaming equivalent of a filesystem. We spent some time comparing two types of message brokers: AMQP/JMS-style message broker The broker assigns individual messages to consumers, and consumers acknowledge individual messages
when they have been successfully processed. Messages are deleted from the broker once they have
been acknowledged. This approach is appropriate as an asynchronous form of RPC (see also
[“Message-Passing Dataflow”](ch04.html#sec_encoding_dataflow_msg)), for example in a task queue, where the exact order of message
processing is not important and where there is no need to go back and read old messages again
after they have been processed.