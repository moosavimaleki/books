##### Replication and Durability 
Historically, durability meant writing to an archive tape. Then it was understood as writing to a disk
or SSD. More recently, it has been adapted to mean replication. Which implementation is better? The truth is, nothing is perfect: *  If you write to disk and the machine dies, even though your data isn’t lost, it is inaccessible
until you either fix the machine or transfer the disk to another machine. Replicated systems can
remain available. *  
A correlated fault—a power outage or a bug that crashes every node on a particular input—can
knock out all replicas at once (see [“Reliability”](ch01.html#sec_introduction_reliability)), losing any data that is
only in memory. Writing to disk is therefore still relevant for in-memory databases. *  In an asynchronously replicated system, recent writes may be lost when the leader becomes
unavailable (see [“Handling Node Outages”](ch05.html#sec_replication_failover)). *  When the power is suddenly cut, SSDs in particular have been shown to sometimes violate the
guarantees they are supposed to provide: even fsync isn’t guaranteed to work correctly
[[12](ch07.html#Zheng2013up)].
Disk firmware can have bugs, just like any other kind of software
[[13](ch07.html#Denness2015tz), [14](ch07.html#Surak2015tz)].