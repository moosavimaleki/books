There are a number of situations in which it is important for nodes to agree. For example: Leader election 
In a database with single-leader replication, all nodes need to agree on which node is the leader.
The leadership position might become contested if some nodes can’t communicate with others due to
a network fault. In this case, consensus is important to avoid a bad failover, resulting in a
split brain situation in which two nodes both believe themselves to be the leader (see
[“Handling Node Outages”](ch05.html#sec_replication_failover)). If there were two leaders, they would both accept writes and their
data would diverge, leading to inconsistency and data loss. Atomic commit 
In a database that supports transactions spanning several nodes or partitions, we have the problem
that a transaction may fail on some nodes but succeed on others. If we want to maintain
transaction atomicity (in the sense of ACID; see [“Atomicity”](ch07.html#sec_transactions_acid_atomicity)), we have to get
all nodes to agree on the outcome of the transaction: either they all abort/roll back (if anything
goes wrong) or they all commit (if nothing goes wrong). This instance of consensus is known as the
atomic commit problem.[xii](ch09.html#idm140605759344208)