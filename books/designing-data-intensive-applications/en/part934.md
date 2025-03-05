The same idea works in the context of log-based message brokers and change data capture. If the CDC
system is set up such that every change has a primary key, and every update for a key replaces the
previous value for that key, then it’s sufficient to keep just the most recent write for a
particular key. Now, whenever you want to rebuild a derived data system such as a search index, you can start a new
consumer from offset 0 of the log-compacted topic, and sequentially scan over all messages in the
log. The log is guaranteed to contain the most recent value for every key in the database (and maybe
some older values)—in other words, you can use it to obtain a full copy of the database contents without
having to take another snapshot of the CDC source database. 
This log compaction feature is supported by Apache Kafka. As we shall see later in this chapter, it
allows the message broker to be used for durable storage, not just for transient messaging.