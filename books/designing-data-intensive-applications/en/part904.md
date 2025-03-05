
Within this publish/subscribe model, different systems take a wide range of approaches, and there
is no one right answer for all purposes. To differentiate the systems, it is particularly helpful to
ask the following two questions: 1.  What happens if the producers send messages faster than the consumers can process them?
Broadly speaking, there are three options: the system can drop messages, buffer messages in a queue,
or apply backpressure (also known as flow control; i.e., blocking the producer from sending more
messages). For example, Unix pipes and TCP use backpressure: they have a small fixed-size buffer,
and if it fills up, the sender is blocked until the recipient takes data out of the buffer (see
[“Network congestion and queueing”](ch08.html#sec_distributed_congestion)). If messages are buffered in a queue, it is important to understand what happens as that queue grows.
Does the system crash if the queue no longer fits in memory, or does it write messages to disk? If
so, how does the disk access affect the performance of the messaging system
[[6](ch11.html#Sackman2016ws)]?