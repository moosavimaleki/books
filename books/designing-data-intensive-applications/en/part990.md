Log-based message broker The broker assigns all messages in a partition to the same consumer node, and always delivers
messages in the same order. Parallelism is achieved through partitioning, and consumers track
their progress by checkpointing the offset of the last message they have processed. The broker
retains messages on disk, so it is possible to jump back and reread old messages if necessary. The log-based approach has similarities to the replication logs found in databases (see
[Chapter 5](ch05.html#ch_replication)) and log-structured storage engines (see [Chapter 3](ch03.html#ch_storage)). We saw that this
approach is especially appropriate for stream processing systems that consume input streams and
generate derived state or derived output streams. In terms of where streams come from, we discussed several possibilities: user activity events,
sensors providing periodic readings, and data feeds (e.g., market data in finance) are naturally
represented as streams. We saw that it can also be useful to think of the writes to a database as a
stream: we can capture the changelog—i.e., the history of all changes made to a database—either
implicitly through change data capture or explicitly through event sourcing. Log compaction allows
the stream to retain a full copy of the contents of a database.