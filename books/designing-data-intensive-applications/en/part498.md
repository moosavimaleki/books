Even though this seems like an obvious idea, database designers only fairly recently—around
2007—decided that a single-threaded loop for executing transactions was feasible
[[45](ch07.html#Stonebraker2007ub_ch7)].
If multi-threaded concurrency was considered essential for getting good performance during the
previous 30 years, what changed to make single-threaded execution possible? Two developments caused this rethink: *  
RAM became cheap enough that for many use cases is now feasible to keep the entire
active dataset in memory (see [“Keeping everything in memory”](ch03.html#sec_storage_inmemory)). When all data that a transaction needs to
access is in memory, transactions can execute much faster than if they have to wait for data to be
loaded from disk. *  
Database designers realized that OLTP transactions are usually short and only make a small number
of reads and writes (see [“Transaction Processing or Analytics?”](ch03.html#sec_storage_analytics)). By contrast, long-running analytic queries
are typically read-only, so they can be run on a consistent snapshot (using snapshot isolation)
outside of the serial execution loop.