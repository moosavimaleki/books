Thus, a sloppy quorum actually isn’t a quorum at all in the traditional sense. It’s only an
assurance of durability, namely that the data is stored on w nodes somewhere. There is no
guarantee that a read of r nodes will see it until the hinted handoff has completed. 
Sloppy quorums are optional in all common Dynamo implementations. In Riak they are enabled by
default, and in Cassandra and Voldemort they are disabled by default
[[46](ch05.html#Blomstedt2012vf), [49](ch05.html#Ellis2012wm),
[50](ch05.html#VoldemortWiki)]. ### Multi-datacenter operation 
We previously discussed cross-datacenter replication as a use case for multi-leader replication (see
[“Multi-Leader Replication”](#sec_replication_multi_leader)). Leaderless replication is also suitable for
multi-datacenter operation, since it is designed to tolerate conflicting concurrent writes, network
interruptions, and latency spikes. 
Cassandra and Voldemort implement their multi-datacenter support within the normal leaderless model:
the number of replicas n includes nodes in all datacenters, and in the configuration you can
specify how many of the n replicas you want to have in each datacenter. Each write from a client
is sent to all replicas, regardless of datacenter, but the client usually only waits for
acknowledgment from a quorum of nodes within its local datacenter so that it is unaffected by
delays and interruptions on the cross-datacenter link. The higher-latency writes to other
datacenters are often configured to happen asynchronously, although there is some flexibility in the
configuration [[50](ch05.html#VoldemortWiki),
[51](ch05.html#Cassandra20)].