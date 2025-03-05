This voting process looks superficially similar to two-phase commit. The biggest differences are
that in 2PC the coordinator is not elected, and that fault-tolerant consensus algorithms only
require votes from a majority of nodes, whereas 2PC requires a “yes” vote from every participant.
Moreover, consensus algorithms define a recovery process by which nodes can get into a consistent
state after a new leader is elected, ensuring that the safety properties are always met. These
differences are key to the correctness and fault tolerance of a consensus algorithm. ### Limitations of consensus Consensus algorithms are a huge breakthrough for distributed systems: they bring concrete safety
properties (agreement, integrity, and validity) to systems where everything else is uncertain, and
they nevertheless remain fault-tolerant (able to make progress as long as a majority of nodes are
working and reachable). They provide total order broadcast, and therefore they can also implement
linearizable atomic operations in a fault-tolerant way (see [“Implementing linearizable storage using total order broadcast”](#sec_consistency_abcast_to_lin)).