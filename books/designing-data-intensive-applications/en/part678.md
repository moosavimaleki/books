*  Serializability, which we discussed in [Chapter 7](ch07.html#ch_transactions), is about ensuring that transactions
behave as if they were executed in some sequential order. It can be achieved by literally
executing transactions in that serial order, or by allowing concurrent execution while preventing
serialization conflicts (by locking or aborting). *  The use of timestamps and clocks in distributed systems that we discussed in [Chapter 8](ch08.html#ch_distributed)
(see [“Relying on Synchronized Clocks”](ch08.html#sec_distributed_clocks_relying)) is another attempt to introduce order into a disorderly
world, for example to determine which one of two writes happened later. It turns out that there are deep connections between ordering, linearizability, and consensus.
Although this notion is a bit more theoretical and abstract than the rest of this book, it is very
helpful for clarifying our understanding of what systems can and cannot do. We will explore this
topic in the next few sections. ## Ordering and Causality 
There are several reasons why ordering keeps coming up, and one of the reasons is that it helps
preserve causality. We have already seen several examples over the course of this book where
causality has been important: