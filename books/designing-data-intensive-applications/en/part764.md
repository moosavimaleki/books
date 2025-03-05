[viii](ch09.html#idm140605759542720-marker) It is possible to make physical
clock timestamps consistent with causality: in [“Synchronized clocks for global snapshots”](ch08.html#sec_distributed_spanner)
we discussed Google’s Spanner, which estimates the expected clock skew and waits out the
uncertainty interval before committing a write. This method ensures that a causally later transaction is
given a greater timestamp. However, most clocks cannot provide the required uncertainty
metric. [ix](ch09.html#idm140605759485280-marker) The
term atomic broadcast is traditional, but it is very confusing as it’s inconsistent with
other uses of the word atomic: it has nothing to do with atomicity in ACID transactions
and is only indirectly related to atomic operations (in the sense of multi-threaded programming) or
atomic registers (linearizable storage). The term total order multicast is another
synonym. [x](ch09.html#idm140605759439152-marker) In a
formal sense, a linearizable read-write register is an “easier” problem. Total order broadcast is
equivalent to consensus [[67](ch09.html#Chandra1996cp)], which has no
deterministic solution in the asynchronous crash-stop model
[[68](ch09.html#Fischer1985ji)], whereas a linearizable read-write
register can be implemented in the same system model
[[23](ch09.html#Attiya1995bm), [24](ch09.html#Lynch1997gr),
[25](ch09.html#Cachin2011wt)]. However, supporting atomic operations such as
compare-and-set or increment-and-get in a register makes it equivalent to consensus
[[28](ch09.html#Herlihy1991gk)]. Thus,
the problems of consensus and a linearizable register are closely related.