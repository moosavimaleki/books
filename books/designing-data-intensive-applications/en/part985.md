### Atomic commit revisited 
In order to give the appearance of exactly-once processing in the presence of faults, we need to
ensure that all outputs and side effects of processing an event take effect if and only if the
processing is successful. Those effects include any messages sent to downstream operators or
external messaging systems (including email or push notifications), any database writes, any changes
to operator state, and any acknowledgment of input messages (including moving the consumer offset
forward in a log-based message broker). Those things either all need to happen atomically, or none of them must happen, but they should not
go out of sync with each other. If this approach sounds familiar, it is because we discussed it in
[“Exactly-once message processing”](ch09.html#sec_consistency_exactly_once) in the context of distributed transactions and two-phase commit. 
In [Chapter 9](ch09.html#ch_consistency) we discussed the problems in the traditional implementations of distributed
transactions, such as XA. However, in more restricted environments it is possible to implement such
an atomic commit facility efficiently. This approach is used in Google Cloud Dataflow
[[81](ch11.html#Akidau2013uz),
[92](ch11.html#Tzoumas2015tt)] and VoltDB
[[94](ch11.html#Betts2015ub)],
and there are plans to add similar features to Apache Kafka
[[95](ch11.html#Junqueira2016vv), [96](ch11.html#Gustafson2016na)]. Unlike XA, these implementations do not attempt to provide transactions across heterogeneous technologies, but instead keep them internal by managing both state changes and messaging within the stream processing framework. The overhead of the transaction protocol can be amortized by processing several input
messages within a single transaction.