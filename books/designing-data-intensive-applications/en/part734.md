*  
For database-internal distributed transactions (not XA), the limitations are not so great—for
example, a distributed version of SSI is possible. However, there remains the problem that for 2PC
to successfully commit a transaction, all participants must respond. Consequently, if any part
of the system is broken, the transaction also fails. Distributed transactions thus have a tendency
of amplifying failures, which runs counter to our goal of building fault-tolerant systems. Do these facts mean we should give up all hope of keeping several systems consistent with each
other? Not quite—there are alternative methods that allow us to achieve the same thing without
the pain of heterogeneous distributed transactions. We will return to these in Chapters
[11](ch11.html#ch_stream)
and   [12](ch12.html#ch_future).
But first, we should wrap up the topic of consensus. ## Fault-Tolerant Consensus 
Informally, consensus means getting several nodes to agree on something. For example, if several
people concurrently try to book the last seat on an airplane, or the same seat in a theater, or try
to register an account with the same username, then a consensus algorithm could be used to determine
which one of these mutually incompatible operations should be the winner.