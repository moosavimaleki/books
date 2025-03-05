
Nevertheless, they are not used everywhere, because the benefits come at a cost. The process by which nodes vote on proposals before they are decided is a kind of synchronous
replication. As discussed in [“Synchronous Versus Asynchronous Replication”](ch05.html#sec_replication_sync_async), databases are often configured to use
asynchronous replication. In this configuration, some committed data can potentially be lost on
failover—but many people choose to accept this risk for the sake of better performance. Consensus systems always require a strict majority to operate. This means you need a minimum of
three nodes in order to tolerate one failure (the remaining two out of three form a majority), or a
minimum of five nodes to tolerate two failures (the remaining three out of five form a majority). If
a network failure cuts off some nodes from the rest, only the majority portion of the network can
make progress, and the rest is blocked (see also [“The Cost of Linearizability”](#sec_linearizability_cost)).