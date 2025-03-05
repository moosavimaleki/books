On the other hand, if single-leader replication is used, then the leader must be in one of the
datacenters. Any writes and any linearizable reads must be sent to the leader—thus, for any
clients connected to a follower datacenter, those read and write requests must be sent synchronously
over the network to the leader datacenter. If the network between datacenters is interrupted in a single-leader setup, clients connected to
follower datacenters cannot contact the leader, so they cannot make any writes to the database, nor
any linearizable reads. They can still make reads from the follower, but they might be stale
(nonlinearizable). If the application requires linearizable reads and writes, the network
interruption causes the application to become unavailable in the datacenters that cannot contact the
leader. If clients can connect directly to the leader datacenter, this is not a problem, since the
application continues to work normally there. But clients that can only reach a follower datacenter
will experience an outage until the network link is repaired.