We briefly touched on some techniques for conflict resolution in
[“Handling Write Conflicts”](#sec_replication_write_conflicts). Before we wrap up this chapter, let’s explore the issue in a
bit more detail. ### Last write wins (discarding concurrent writes) 
One approach for achieving eventual convergence is to declare that each replica need only store the
most “recent” value and allow “older” values to be overwritten and discarded. Then, as long as we
have some way of unambiguously determining which write is more “recent,” and every write is
eventually copied to every replica, the replicas will eventually converge to the same value. As indicated by the quotes around “recent,” this idea is actually quite misleading. In the
example of [Figure 5-12](#fig_replication_concurrency), neither client knew about the other one when it sent its
write requests to the database nodes, so it’s not clear which one happened first. In fact, it
doesn’t really make sense to say that either happened “first”: we say the writes are concurrent,
so their order is undefined.