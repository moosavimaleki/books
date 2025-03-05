*  
What is the right timeout before the leader is declared dead? A longer timeout means a longer
time to recovery in the case where the leader fails. However, if the timeout is too short, there
could be unnecessary failovers. For example, a temporary load spike could cause a node’s response
time to increase above the timeout, or a network glitch could cause delayed packets. If the system
is already struggling with high load or network problems, an unnecessary failover is likely to
make the situation worse, not better. There are no easy solutions to these problems. For this reason, some operations teams prefer to
perform failovers manually, even if the software supports automatic failover. These issues—node failures; unreliable networks; and trade-offs around replica consistency,
durability, availability, and latency—are in fact fundamental problems in distributed systems.
In [Chapter 8](ch08.html#ch_distributed) and [Chapter 9](ch09.html#ch_consistency) we will discuss them in greater depth. ## Implementation of Replication Logs