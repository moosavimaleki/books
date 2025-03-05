
If you store the changelog durably, that simply has the effect of making the state reproducible. If
you consider the log of events to be your system of record, and any mutable state as being derived
from it, it becomes easier to reason about the flow of data through a system. As Pat Helland puts it
[[52](ch11.html#Helland2015vx)]: 
Transaction logs record all the changes made to the database. High-speed appends are the only way to
change the log. From this perspective, the contents of the database hold a caching of the latest
record values in the logs. The truth is the log. The database is a cache of a subset of the log.
That cached subset happens to be the latest value of each record and index value from the log. 
Log compaction, as discussed in [“Log compaction”](#sec_stream_log_compaction), is one way of bridging the
distinction between log and database state: it retains only the latest version of each record, and
discards overwritten versions.