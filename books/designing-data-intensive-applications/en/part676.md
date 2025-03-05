
Why make this trade-off? It makes no sense to use the CAP theorem to justify the multi-core memory
consistency model: within one computer we usually assume reliable communication, and we don’t expect
one CPU core to be able to continue operating normally if it is disconnected from the rest of the
computer. The reason for dropping linearizability is performance, not fault tolerance. The same is true of many distributed databases that choose not to provide linearizable guarantees:
they do so primarily to increase performance, not so much for fault tolerance
[[46](ch09.html#Abadi2012hb)].
Linearizability is slow—and this is true all the time, not only during a network fault. Can’t we maybe find a more efficient implementation of linearizable storage? It seems the answer is
no: Attiya and Welch [[47](ch09.html#Attiya1994gw)]
prove that if you want linearizability, the response time of read and write requests is at least
proportional to the uncertainty of delays in the network. In a network with highly variable delays,
like most computer networks (see [“Timeouts and Unbounded Delays”](ch08.html#sec_distributed_queueing)), the response time of linearizable
reads and writes is inevitably going to be high. A faster algorithm for linearizability does not
exist, but weaker consistency models can be much faster, so this trade-off is important for
latency-sensitive systems. In [Chapter 12](ch12.html#ch_future) we will discuss some approaches for avoiding
linearizability without sacrificing correctness.