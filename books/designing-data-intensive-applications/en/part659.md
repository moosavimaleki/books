Linearizability Linearizability is a recency guarantee on reads and writes of a register (an individual object).
It doesn’t group operations together into transactions, so it does not prevent problems such as
write skew (see [“Write Skew and Phantoms”](ch07.html#sec_transactions_write_skew)), unless you take additional measures such as
materializing conflicts (see [“Materializing conflicts”](ch07.html#sec_transactions_materializing_conflicts)). 
A database may provide both serializability and linearizability, and this combination is known as
strict serializability or strong one-copy serializability (strong-1SR)
[[4](ch09.html#Bailis2014vc_ch9),
[13](ch09.html#Bernstein1987va_ch9)]. Implementations of serializability
based on two-phase locking (see [“Two-Phase Locking (2PL)”](ch07.html#sec_transactions_2pl)) or actual serial execution (see
[“Actual Serial Execution”](ch07.html#sec_transactions_serial)) are typically linearizable. 
However, serializable snapshot isolation (see [“Serializable Snapshot Isolation (SSI)”](ch07.html#sec_transactions_ssi)) is not linearizable: by
design, it makes reads from a consistent snapshot, to avoid lock contention between readers and
writers. The whole point of a consistent snapshot is that it does not include writes that are more
recent than the snapshot, and thus reads from the snapshot are not linearizable.