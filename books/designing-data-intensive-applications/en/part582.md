Nevertheless, the timestamps in [Figure 8-3](#fig_distributed_timestamps) fail to order the events correctly:
the write x = 1 has a timestamp of 42.004 seconds, but the write x = 2
has a timestamp of 42.003 seconds, even though x = 2 occurred unambiguously later.
When node 2 receives these two events, it will incorrectly conclude that x = 1 is the
more recent value and drop the write x = 2. In effect, client B’s increment operation
will be lost. 
This conflict resolution strategy is called last write wins (LWW), and it is widely used in both
multi-leader replication and leaderless databases such as Cassandra
[[53](ch08.html#Kingsbury2013ti_ch8)] and Riak
[[54](ch08.html#Daily2013te_ch8)] (see
[“Last write wins (discarding concurrent writes)”](ch05.html#sec_replication_lww)). Some implementations generate timestamps on the client rather than
the server, but this doesn’t change the fundamental problems with LWW: *  Database writes can mysteriously disappear: a node with a lagging clock is unable to overwrite
values previously written by a node with a fast clock until the clock skew between the nodes has
elapsed [[54](ch08.html#Daily2013te_ch8),
[55](ch08.html#Kingsbury2013vs)]. This scenario can cause arbitrary
amounts of data to be silently dropped without any error being reported to the application.