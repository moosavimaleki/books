That is the intuition behind linearizability; the formal definition
[[6](ch09.html#Herlihy1990jq)] describes it more precisely. It is
possible (though computationally expensive) to test whether a system’s behavior is linearizable by
recording the timings of all requests and responses, and checking whether they can be arranged into
a valid sequential order [[11](ch09.html#Kingsbury2014tb)]. ##### Linearizability Versus Serializability 
Linearizability is easily confused with serializability (see [“Serializability”](ch07.html#sec_transactions_serializability)),
as both words seem to mean something like “can be arranged in a sequential order.” However, they are
two quite different guarantees, and it is important to distinguish between them: Serializability Serializability is an isolation property of transactions, where every transaction may read and
write multiple objects (rows, documents, records)—see [“Single-Object and Multi-Object Operations”](ch07.html#sec_transactions_multi_object). It
guarantees that transactions behave the same as if they had executed in some serial order (each
transaction running to completion before the next transaction starts). It is okay for that serial
order to be different from the order in which transactions were actually run
[[12](ch09.html#Bailis2014wz)].