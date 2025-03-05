![ddia 0507](assets/ddia_0507.png) ###### Figure 5-7. A write conflict caused by two leaders concurrently updating the same record. ### Synchronous versus asynchronous conflict detection 
In a single-leader database, the second writer will either block and wait for the first write to
complete, or abort the second write transaction, forcing the user to retry the write. On the other
hand, in a multi-leader setup, both writes are successful, and the conflict is only detected
asynchronously at some later point in time. At that time, it may be too late to ask the user to
resolve the conflict. In principle, you could make the conflict detection synchronous—i.e., wait for the write to be
replicated to all replicas before telling the user that the write was successful. However, by doing
so, you would lose the main advantage of multi-leader replication: allowing each replica to accept
writes independently. If you want synchronous conflict detection, you might as well just use
single-leader replication.