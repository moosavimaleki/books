The basic flow of 2PC is illustrated in [Figure 9-9](#fig_consistency_two_phase_commit). Instead of a single
commit request, as with a single-node transaction, the commit/abort process in 2PC is split into two
phases (hence the name). ![ddia 0909](assets/ddia_0909.png) ###### Figure 9-9. A successful execution of two-phase commit (2PC). # Don’t confuse 2PC and 2PL 
Two-phase commit (2PC) and two-phase locking (see [“Two-Phase Locking (2PL)”](ch07.html#sec_transactions_2pl)) are two very
different things. 2PC provides atomic commit in a distributed database, whereas 2PL provides
serializable isolation. To avoid confusion, it’s best to think of them as entirely separate concepts
and to ignore the unfortunate similarity in the names. 
2PC uses a new component that does not normally appear in single-node transactions: a
coordinator (also known as transaction manager). The coordinator is often implemented as a
library within the same application process that is requesting the transaction (e.g., embedded in a
Java EE container), but it can also be a separate process or service. Examples of such coordinators
include Narayana, JOTM, BTM, or MSDTC.