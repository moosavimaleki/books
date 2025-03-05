##### Footnotes [i](ch09.html#idm140605760066128-marker) A
subtle detail of this diagram is that it assumes the existence of a global clock, represented by the
horizontal axis. Even though real systems typically don’t have accurate clocks (see
[“Unreliable Clocks”](ch08.html#sec_distributed_clocks)), this assumption is okay: for the purposes of
analyzing a distributed algorithm, we may pretend that an accurate global clock exists, as long as
the algorithm doesn’t have access to it [[47](ch09.html#Attiya1994gw)].
Instead, the algorithm can only see a mangled approximation of real time, as produced by a quartz
oscillator and NTP. [ii](ch09.html#idm140605760046160-marker) A register in which reads may return
either the old or the new value if they are concurrent with a write is known as a regular
register [[7](ch09.html#Lamport1986cg),
[25](ch09.html#Cachin2011wt)]. [iii](ch09.html#idm140605759949024-marker) Strictly
speaking, ZooKeeper and etcd provide linearizable writes, but reads may be stale, since by default
they can be served by any one of the replicas. You can optionally request a linearizable read: etcd
calls this a quorum read [[16](ch09.html#Etcd)], and in
ZooKeeper you need to call sync() before the read
[[15](ch09.html#Junqueira2013wi_ch9)]; see
[“Implementing linearizable storage using total order broadcast”](#sec_consistency_abcast_to_lin).