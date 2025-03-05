3.  Reconfiguring the system to use the new leader. Clients now need to send
their write requests to the new leader (we discuss this
in [“Request Routing”](ch06.html#sec_partitioning_routing)). If the old leader comes back, it might still believe that it is
the leader, not realizing that the other replicas have
forced it to step down. The system needs to ensure that the old leader becomes a follower and
recognizes the new leader. Failover is fraught with things that can go wrong: *  
If asynchronous replication is used, the new leader may not have received all the writes from the old
leader before it failed. If the former leader rejoins the cluster after a new leader has been
chosen, what should happen to those writes? The new leader may have received conflicting writes
in the meantime. The most common solution is for the old leader’s unreplicated writes to simply be
discarded, which may violate clients’ durability expectations.