
Riak keeps all communication between clients and database nodes local to one datacenter, so n
describes the number of replicas within one datacenter. Cross-datacenter replication between
database clusters happens asynchronously in the background, in a style that is similar to
multi-leader replication
[[52](ch05.html#Riak2014vb)]. ## Detecting Concurrent Writes 
Dynamo-style databases allow several clients to concurrently write to the same key, which means that
conflicts will occur even if strict quorums are used. The situation is similar to multi-leader
replication (see [“Handling Write Conflicts”](#sec_replication_write_conflicts)), although in Dynamo-style databases conflicts
can also arise during read repair or hinted handoff. The problem is that events may arrive in a different order at different nodes, due to variable
network delays and partial failures. For example, [Figure 5-12](#fig_replication_concurrency) shows two clients,
A and B, simultaneously writing to a key X in a three-node datastore: *  Node 1 receives the write from A, but never receives the write from B due to a transient
outage.