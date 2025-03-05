*  Node 2 first receives the write from A, then the write from B. *  Node 3 first receives the write from B, then the write from A. ![ddia 0512](assets/ddia_0512.png) ###### Figure 5-12. Concurrent writes in a Dynamo-style datastore: there is no well-defined ordering. If each node simply overwrote the value for a key whenever it received a write request from a
client, the nodes would become permanently inconsistent, as shown by the final get request in
[Figure 5-12](#fig_replication_concurrency): node 2 thinks that the final value of X is B, whereas the other
nodes think that the value is A. In order to become eventually consistent, the replicas should converge toward the same value. How
do they do that? One might hope that replicated databases would handle this automatically, but
unfortunately most implementations are quite poor: if you want to avoid losing data, you—the
application developer—need to know a lot about the internals of your database’s conflict
handling.