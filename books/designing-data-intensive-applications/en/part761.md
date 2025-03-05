Nevertheless, not every system necessarily requires consensus: for example, leaderless and
multi-leader replication systems typically do not use global consensus. The conflicts that occur in
these systems (see [“Handling Write Conflicts”](ch05.html#sec_replication_write_conflicts)) are a consequence of not having consensus
across different leaders, but maybe that’s okay: maybe we simply need to cope without
linearizability and learn to work better with data that has branching and merging version histories. This chapter referenced a large body of research on the theory of distributed systems. Although the
theoretical papers and proofs are not always easy to understand, and sometimes make unrealistic
assumptions, they are incredibly valuable for informing practical work in this field: they help us
reason about what can and cannot be done, and help us find the counterintuitive ways in which
distributed systems are often flawed. If you have the time, the references are well worth exploring. This brings us to the end of [Part II](part02.html#part_distributed_data) of this book, in which we covered replication
([Chapter 5](ch05.html#ch_replication)), partitioning ([Chapter 6](ch06.html#ch_partitioning)), transactions ([Chapter 7](ch07.html#ch_transactions)),
distributed system failure models ([Chapter 8](ch08.html#ch_distributed)), and finally consistency and consensus
([Chapter 9](#ch_consistency)). Now that we have laid a firm foundation of theory, in [Part III](part03.html#part_systems) we will
turn once again to more practical systems, and discuss how to build powerful applications from
heterogeneous building blocks.