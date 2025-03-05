Weakening durability may sound like a bad trade-off, but asynchronous replication is nevertheless
widely used, especially if there are many followers or if they are geographically distributed. We
will return to this issue in [“Problems with Replication Lag”](#sec_replication_lag). ##### Research on Replication 
It can be a serious problem for asynchronously replicated systems to lose data if the leader fails,
so researchers have continued investigating replication methods that do not lose data but still
provide good performance and availability. For example, chain replication
[[8](ch05.html#vanRenesse2004td_ch5),
[9](ch05.html#Terrace2009vx)] is a variant of synchronous replication
that has been successfully implemented in a few systems such as Microsoft Azure Storage
[[10](ch05.html#Calder2011to),
[11](ch05.html#Wang2016vy)]. 
There is a strong connection between consistency of replication and consensus (getting several
nodes to agree on a value), and we will explore this area of theory in more detail in
[Chapter 9](ch09.html#ch_consistency). In this chapter we will concentrate on the simpler forms of replication that are
most commonly used in databases in practice.