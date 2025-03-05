
Now imagine that the unavailable node comes back online, and clients start reading from it. Any
writes that happened while the node was down are missing from that node. Thus, if you read from that
node, you may get stale (outdated) values as responses. To solve that problem, when a client reads from the database, it doesn’t just send its request to
one replica: read requests are also sent to several nodes in parallel. The client may get
different responses from different nodes; i.e., the up-to-date value from one node and a stale value
from another. Version numbers are used to determine which value is newer (see
[“Detecting Concurrent Writes”](#sec_replication_concurrent)). ### Read repair and anti-entropy 
The replication scheme should ensure that eventually all the data is copied to every replica. After
an unavailable node comes back online, how does it catch up on the writes that it missed? Two mechanisms are often used in Dynamo-style datastores: