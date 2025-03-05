
Leader-based replication requires all writes to go through a single node, but read-only queries can
go to any replica. For workloads that consist of mostly reads and only a small percentage of writes
(a common pattern on the web), there is an attractive option: create many followers, and distribute
the read requests across those followers. This removes load from the leader and allows read requests to be
served by nearby replicas. In this read-scaling architecture, you can increase the capacity for serving read-only requests
simply by adding more followers. However, this approach only realistically works with asynchronous
replication—if you tried to synchronously replicate to all followers, a single node failure or
network outage would make the entire system unavailable for writing. And the more nodes you have,
the likelier it is that one will be down, so a fully synchronous configuration would be very unreliable. 
Unfortunately, if an application reads from an asynchronous follower, it may see outdated
information if the follower has fallen behind. This leads to apparent inconsistencies in the
database: if you run the same query on the leader and a follower at the same time, you may get
different results, because not all writes have been reflected in the follower. This inconsistency is
just a temporary state—if you stop writing to the database and wait a while, the followers will
eventually catch up and become consistent with the leader. For that reason, this effect is known
as eventual consistency [[22](ch05.html#Vogels2008ey),
[23](ch05.html#Terry2011vp)].[iii](ch05.html#idm140605776151312)