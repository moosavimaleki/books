An application may initially run only on a single node, but eventually may grow to thousands of
nodes. Trying to perform majority votes over so many nodes would be terribly inefficient. Instead,
ZooKeeper runs on a fixed number of nodes (usually three or five) and performs its majority votes
among those nodes while supporting a potentially large number of clients. Thus, ZooKeeper provides a
way of “outsourcing” some of the work of coordinating nodes (consensus, operation ordering, and
failure detection) to an external service. 
Normally, the kind of data managed by ZooKeeper is quite slow-changing: it represents information
like “the node running on 10.1.1.23 is the leader for partition 7,” which may change on a timescale
of minutes or hours. It is not intended for storing the runtime state of the application, which may
change thousands or even millions of times per second. If application state needs to be replicated
from one node to another, other tools (such as Apache BookKeeper
[[108](ch09.html#Kelly2014lq)]) can be used.