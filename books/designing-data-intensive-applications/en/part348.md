## Multi-Leader Replication Topologies 
A replication topology describes the communication paths along which writes are propagated from
one node to another. If you have two leaders, like in [Figure 5-7](#fig_replication_write_conflict), there is
only one plausible topology: leader 1 must send all of its writes to leader 2, and vice versa. With
more than two leaders, various different topologies are possible. Some examples are illustrated in
[Figure 5-8](#fig_replication_topologies). ![ddia 0508](assets/ddia_0508.png) ###### Figure 5-8. Three example topologies in which multi-leader replication can be set up. 
The most general topology is all-to-all ([Figure 5-8](#fig_replication_topologies) [c]), in which every
leader sends its writes to every other leader. However, more restricted topologies are also used:
for example, MySQL by default supports only a circular topology
[[34](ch05.html#Hodges2013vb)],
in which each node receives writes from one node and forwards those writes (plus any writes of its
own) to one other node. Another popular topology has the shape of a
star:[v](ch05.html#idm140605775851008) one
designated root node forwards writes to all of the other nodes. The star topology can be generalized
to a tree.