*  Only one node is allowed to be the leader for a database partition, to avoid split brain (see
[“Handling Node Outages”](ch05.html#sec_replication_failover)). *  Only one transaction or client is allowed to hold the lock for a particular resource or object, to
prevent concurrently writing to it and corrupting it. *  Only one user is allowed to register a particular username, because a username must uniquely
identify a user. Implementing this in a distributed system requires care: even if a node believes that it is “the
chosen one” (the leader of the partition, the holder of the lock, the request handler of the user
who successfully grabbed the username), that doesn’t necessarily mean a quorum of nodes agrees!
A node may have formerly been the leader, but if the other nodes declared it dead in the meantime
(e.g., due to a network interruption or GC pause), it may have been demoted and another leader may
have already been elected.