
One option is to keep the state in a remote datastore and replicate it, although having to query a
remote database for each individual message can be slow, as discussed in [“Stream-table join (stream enrichment)”](#sec_stream_table_joins).
An alternative is to keep state local to the stream processor, and replicate it periodically. Then,
when the stream processor is recovering from a failure, the new task can read the replicated state
and resume processing without data loss. 
For example, Flink periodically captures snapshots of operator state and writes them to durable
storage such as HDFS [[92](ch11.html#Tzoumas2015tt),
[93](ch11.html#Carbone2015wh)]; Samza and Kafka Streams replicate state
changes by sending them to a dedicated Kafka topic with log compaction, similar to change data
capture [[84](ch11.html#SamzaState),
[100](ch11.html#Warski2016tm)].
VoltDB replicates state by redundantly processing each input message on several nodes (see
[“Actual Serial Execution”](ch07.html#sec_transactions_serial)). In some cases, it may not even be necessary to replicate the state, because it can be rebuilt from
the input streams. For example, if the state consists of aggregations over a fairly short window, it
may be fast enough to simply replay the input events corresponding to that window. If the state is a
local replica of a database, maintained by change data capture, the database can also be rebuilt
from the log-compacted change stream (see [“Log compaction”](#sec_stream_log_compaction)).