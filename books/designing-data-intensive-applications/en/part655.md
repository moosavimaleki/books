In [Figure 9-4](#fig_consistency_linearizability_3) we add a third type of operation besides read and
write: *  cas(x, vold, vnew) ⇒ r means the client
requested an atomic compare-and-set operation (see [“Compare-and-set”](ch07.html#sec_transactions_compare_and_set)). If the
current value of the register x equals vold, it should be atomically set to vnew. If
x ≠ vold then the operation should leave the register unchanged and
return an error. r is the database’s response (ok or error). Each operation in [Figure 9-4](#fig_consistency_linearizability_3) is marked with a vertical line (inside the
bar for each operation) at the time when we think the operation was executed. Those markers are
joined up in a sequential order, and the result must be a valid sequence of reads and writes for a
register (every read must return the value set by the most recent write). The requirement of linearizability is that the lines joining up the operation markers always move
forward in time (from left to right), never backward. This requirement ensures the recency guarantee we
discussed earlier: once a new value has been written or read, all subsequent reads see the value
that was written, until it is overwritten again.