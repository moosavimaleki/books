Read repair When a client makes a read from several nodes in parallel, it can detect any stale responses.
For example, in [Figure 5-10](#fig_replication_quorum_node_outage), user 2345 gets a version 6 value from
replica 3 and a version 7 value from replicas 1 and 2. The client sees that replica 3 has a stale
value and writes the newer value back to that replica. This approach works well for values that are
frequently read. Anti-entropy process In addition, some datastores have a background process that constantly looks for differences in
the data between replicas and copies any missing data from one replica to another. Unlike the
replication log in leader-based replication, this anti-entropy process does not copy writes in
any particular order, and there may be a significant delay before data is copied. 
Not all systems implement both of these; for example, Voldemort currently does not have an
anti-entropy process. Note that without an anti-entropy process, values that are rarely read may be
missing from some replicas and thus have reduced durability, because read repair is only performed
when a value is read by the application.