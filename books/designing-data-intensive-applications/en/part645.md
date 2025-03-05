Researchers in the field of distributed systems have been studying these topics for decades, so
there is a lot of material—we’ll only be able to scratch the surface. In this book we don’t have
space to go into details of the formal models and proofs, so we will stick with informal intuitions.
The literature references offer plenty of additional depth if you’re interested. # Consistency Guarantees In [“Problems with Replication Lag”](ch05.html#sec_replication_lag) we looked at some timing issues that occur in a replicated database. If
you look at two database nodes at the same moment in time, you’re likely to see different data on
the two nodes, because write requests arrive on different nodes at different times. These
inconsistencies occur no matter what replication method the database uses (single-leader,
multi-leader, or leaderless replication). 
Most replicated databases provide at least eventual consistency, which means that if you stop
writing to the database and wait for some unspecified length of time, then eventually all read
requests will return the same value [[1](ch09.html#Bailis2013jc_ch9)].
In other words, the inconsistency is temporary, and it eventually resolves itself (assuming that any
faults in the network are also eventually repaired). A better name for eventual consistency may be
convergence, as we expect all replicas to eventually converge to the same value
[[2](ch09.html#Mahajan2011wz)].