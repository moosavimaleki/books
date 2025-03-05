### The CAP theorem 
This issue is not just a consequence of single-leader and multi-leader replication: any linearizable
database has this problem, no matter how it is implemented. The issue also isn’t specific to
multi-datacenter deployments, but can occur on any unreliable network, even within one datacenter.
The trade-off is as follows:[v](ch09.html#idm140605759796128) *  If your application requires linearizability, and some replicas are disconnected from the other
replicas due to a network problem, then some replicas cannot process requests while they are
disconnected: they must either wait until the network problem is fixed, or return an error (either
way, they become unavailable). *  If your application does not require linearizability, then it can be written in a way that each
replica can process requests independently, even if it is disconnected from other replicas (e.g.,
multi-leader). In this case, the application can remain available in the face of a network
problem, but its behavior is not linearizable.