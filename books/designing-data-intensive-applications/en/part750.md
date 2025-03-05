Change notifications Not only can one client read locks and values that were created by another client, but it can also
watch them for changes. Thus, a client can find out when another client joins the cluster (based
on the value it writes to ZooKeeper), or if another client fails (because its session times out
and its ephemeral nodes disappear). By subscribing to notifications, a client avoids having to
frequently poll to find out about changes. Of these features, only the linearizable atomic operations really require consensus. However, it is
the combination of these features that makes systems like ZooKeeper so useful for distributed
coordination. ### Allocating work to nodes 
One example in which the ZooKeeper/Chubby model works well is if you have several instances of a
process or service, and one of them needs to be chosen as leader or primary. If the leader fails,
one of the other nodes should take over. This is of course useful for single-leader databases, but
it’s also useful for job schedulers and similar stateful systems.