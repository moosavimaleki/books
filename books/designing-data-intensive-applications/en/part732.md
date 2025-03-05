
Many XA implementations have an emergency escape hatch called heuristic decisions: allowing a
participant to unilaterally decide to abort or commit an in-doubt transaction without a definitive
decision from the coordinator [[76](ch09.html#XASpec1991vk),
[77](ch09.html#Spille2004vr),
[91](ch09.html#SQLServerInDoubt)]. To be clear, heuristic here is a euphemism for probably breaking atomicity,
since it violates the system of promises in two-phase commit. Thus, heuristic decisions are intended
only for getting out of catastrophic situations, and not for regular use. ### Limitations of distributed transactions 
XA transactions solve the real and important problem of keeping several participant data systems
consistent with each other, but as we have seen, they also introduce major operational problems. In
particular, the key realization is that the transaction coordinator is itself a kind of database (in
which transaction outcomes are stored), and so it needs to be approached with the same care as any
other important database: *  If the coordinator is not replicated but runs only on a single machine, it is a single point of
failure for the entire system (since its failure causes other application servers to block on
locks held by in-doubt transactions). Surprisingly, many coordinator implementations are not
highly available by default, or have only rudimentary replication support.