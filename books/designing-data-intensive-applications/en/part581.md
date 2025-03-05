### Timestamps for ordering events 
Let’s consider one particular situation in which it is tempting, but dangerous, to rely on clocks:
ordering of events across multiple nodes. For example, if two clients write to a distributed
database, who got there first? Which write is the more recent one? [Figure 8-3](#fig_distributed_timestamps) illustrates a dangerous use of time-of-day clocks in a database with
multi-leader replication (the example is similar to [Figure 5-9](ch05.html#fig_replication_causality)). Client A writes
x = 1 on node 1; the write is replicated to node 3; client B increments x on node
3 (we now have x = 2); and finally, both writes are replicated to node 2. ![ddia 0803](assets/ddia_0803.png) ###### Figure 8-3. The write by client B is causally later than the write by client A, but B’s write has an earlier timestamp. 
In [Figure 8-3](#fig_distributed_timestamps), when a write is replicated to other nodes, it is tagged with a
timestamp according to the time-of-day clock on the node where the write originated. The clock
synchronization is very good in this example: the skew between node 1 and node 3 is less than
3 ms, which is probably better than you can expect in practice.