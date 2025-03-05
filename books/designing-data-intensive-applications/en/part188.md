As RAM becomes cheaper, the cost-per-gigabyte argument is eroded. Many datasets are simply not that
big, so it’s quite feasible to keep them entirely in memory, potentially distributed across several
machines. This has led to the development of in-memory databases. 
Some in-memory key-value stores, such as Memcached, are intended for caching use only, where it’s
acceptable for data to be lost if a machine is restarted. But other in-memory databases aim for
durability, which can be achieved with special hardware (such as battery-powered RAM), by writing a
log of changes to disk, by writing periodic snapshots to disk, or by replicating the in-memory state
to other machines. When an in-memory database is restarted, it needs to reload its state, either from disk or over the
network from a replica (unless special hardware is used). Despite writing to disk, it’s still an
in-memory database, because the disk is merely used as an append-only log for durability, and reads
are served entirely from memory. Writing to disk also has operational advantages: files on disk can
easily be backed up, inspected, and analyzed by external utilities.