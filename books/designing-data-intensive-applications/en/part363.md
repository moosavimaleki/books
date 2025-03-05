### Monitoring staleness 
From an operational perspective, it’s important to monitor whether your databases are
returning up-to-date results. Even if your application can tolerate stale reads, you need to be
aware of the health of your replication. If it falls behind significantly, it should alert you so
that you can investigate the cause (for example, a problem in the network or an overloaded node). For leader-based replication, the database typically exposes metrics for the replication lag, which
you can feed into a monitoring system. This is possible because writes are applied to the leader and
to followers in the same order, and each node has a position in the replication log (the number of
writes it has applied locally). By subtracting a follower’s current position from the leader’s
current position, you can measure the amount of replication lag. However, in systems with leaderless replication, there is no fixed order in which writes are
applied, which makes monitoring more difficult. Moreover, if the database only uses read repair (no
anti-entropy), there is no limit to how old a value might be—if a value is only infrequently
read, the value returned by a stale replica may be ancient.