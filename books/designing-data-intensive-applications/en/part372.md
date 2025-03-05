The only safe way of using a database with LWW is to ensure that a key is only written once and
thereafter treated as immutable, thus avoiding any concurrent updates to the same key. For example,
a recommended way of using Cassandra is to use a UUID as the key, thus giving each write operation a
unique key [[53](ch05.html#Ellis2013ug)]. ### The “happens-before” relationship and concurrency 
How do we decide whether two operations are concurrent or not? To develop an intuition, let’s look
at some examples: *  In [Figure 5-9](#fig_replication_causality), the two writes are not concurrent: A’s insert happens before
B’s increment, because the value incremented by B is the value inserted by A. In other words, B’s
operation builds upon A’s operation, so B’s operation must have happened later.
We also say that B is causally dependent on A. *  On the other hand, the two writes in [Figure 5-12](#fig_replication_concurrency) are concurrent: when each
client starts the operation, it does not know that another client is also performing an operation
on the same key. Thus, there is no causal dependency between the operations.