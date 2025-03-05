The snapshot of the database must correspond to a known position or offset in the change log, so
that you know at which point to start applying changes after the snapshot has been processed. Some
CDC tools integrate this snapshot facility, while others leave it as a manual operation. ### Log compaction 
If you can only keep a limited amount of log history, you need to go through the snapshot process
every time you want to add a new derived data system. However, log compaction provides a good
alternative. We discussed log compaction previously in [“Hash Indexes”](ch03.html#sec_storage_hash_index), in the context of
log-structured storage engines (see [Figure 3-2](ch03.html#fig_storage_compaction) for an example). The principle is
simple: the storage engine periodically looks for log records with the same key, throws away any
duplicates, and keeps only the most recent update for each key. This compaction and merging process
runs in the background. 
In a log-structured storage engine, an update with a special null value (a tombstone) indicates
that a key was deleted, and causes it to be removed during log compaction. But as long as a key is
not overwritten or deleted, it stays in the log forever. The disk space required for such a
compacted log depends only on the current contents of the database, not the number of writes that
have ever occurred in the database. If the same key is frequently overwritten, previous values will
eventually be garbage-collected, and only the latest value will be retained.