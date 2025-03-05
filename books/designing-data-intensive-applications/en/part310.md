How do you achieve high availability with leader-based replication? ### Follower failure: Catch-up recovery On its local disk, each follower keeps a log of the data changes it has received from the leader. If
a follower crashes and is restarted, or if the network between the leader and the follower is
temporarily interrupted, the follower can recover quite easily: from its log, it knows the last
transaction that was processed before the fault occurred. Thus, the follower can connect to the
leader and request all the data changes that occurred during the time when the follower was
disconnected. When it has applied these changes, it has caught up to the leader and can continue
receiving a stream of data changes as before. ### Leader failure: Failover 
Handling a failure of the leader is trickier: one of the followers needs to be promoted to be the
new leader, clients need to be reconfigured to send their writes to the new leader, and the other
followers need to start consuming data changes from the new leader. This process is called
failover.