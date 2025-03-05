Total ordering of operations 
As discussed in [“The leader and the lock”](ch08.html#sec_distributed_lock_fencing), when some resource is protected by a lock or
lease, you need a fencing token to prevent clients from conflicting with each other in the case
of a process pause. The fencing token is some number that monotonically increases every time the
lock is acquired. ZooKeeper provides this by totally ordering all operations and giving each
operation a monotonically increasing transaction ID (zxid) and version number (cversion)
[[15](ch09.html#Junqueira2013wi_ch9)]. Failure detection 
Clients maintain a long-lived session on ZooKeeper servers, and the client and server periodically
exchange heartbeats to check that the other node is still alive. Even if the connection is
temporarily interrupted, or a ZooKeeper node fails, the session remains active. However, if the
heartbeats cease for a duration that is longer than the session timeout, ZooKeeper declares the
session to be dead. Any locks held by a session can be configured to be automatically released
when the session times out (ZooKeeper calls these ephemeral nodes).