
“Last write wins” conflict resolution methods based on time-of-day clocks (e.g., in Cassandra; see
[“Relying on Synchronized Clocks”](ch08.html#sec_distributed_clocks_relying)) are almost certainly nonlinearizable, because clock timestamps
cannot be guaranteed to be consistent with actual event ordering due to clock skew. Sloppy quorums
([“Sloppy Quorums and Hinted Handoff”](ch05.html#sec_replication_sloppy_quorum)) also ruin any chance of linearizability. Even with strict
quorums, nonlinearizable behavior is possible, as demonstrated in the next section. ### Linearizability and quorums 
Intuitively, it seems as though strict quorum reads and writes should be linearizable in a
Dynamo-style model. However, when we have variable network delays, it is possible to have race
conditions, as demonstrated in [Figure 9-6](#fig_consistency_leaderless). ![ddia 0906](assets/ddia_0906.png) ###### Figure 9-6. A nonlinearizable execution, despite using a strict quorum. In [Figure 9-6](#fig_consistency_leaderless), the initial value of x is 0, and a writer client is updating
x to 1 by sending the write to all three replicas (n = 3, w = 3).
Concurrently, client A reads from a quorum of two nodes (r = 2) and sees the new value 1
on one of the nodes. Also concurrently with the write, client B reads from a different quorum of two
nodes, and gets back the old value 0 from both.