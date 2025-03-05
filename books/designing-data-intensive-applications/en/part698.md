This idea of knowing when your total order is finalized is captured in the topic of total order
broadcast. ## Total Order Broadcast 
If your program runs only on a single CPU core, it is easy to define a total ordering of operations:
it is simply the order in which they were executed by the CPU. However, in a distributed system,
getting all nodes to agree on the same total ordering of operations is tricky. In the last section
we discussed ordering by timestamps or sequence numbers, but found that it is not as powerful as
single-leader replication (if you use timestamp ordering to implement a uniqueness constraint, you
cannot tolerate any faults). 
As discussed, single-leader replication determines a total order of operations by choosing one node
as the leader and sequencing all operations on a single CPU core on the leader. The challenge then
is how to scale the system if the throughput is greater than a single leader can handle, and also
how to handle failover if the leader fails (see [“Handling Node Outages”](ch05.html#sec_replication_failover)). In the
distributed systems literature, this problem is known as total order broadcast or atomic
broadcast [[25](ch09.html#Cachin2011wt),
[57](ch09.html#Defago2004ji),
[58](ch09.html#Attiya2004ke)].[ix](ch09.html#idm140605759485280)