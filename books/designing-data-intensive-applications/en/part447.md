### Durability 
The purpose of a database system is to provide a safe place where data can be stored without fear of
losing it. Durability is the promise that once a transaction has committed successfully, any data it
has written will not be forgotten, even if there is a hardware fault or the database crashes. In a single-node database, durability typically means that the data has been written to nonvolatile
storage such as a hard drive or SSD. It usually also involves a write-ahead log or similar (see
[“Making B-trees reliable”](ch03.html#sec_storage_btree_wal)), which allows recovery in the event that the data structures on disk are
corrupted. In a replicated database, durability may mean that the data has been successfully copied
to some number of nodes. In order to provide a durability guarantee, a database must wait until
these writes or replications are complete before reporting a transaction as successfully committed. As discussed in [“Reliability”](ch01.html#sec_introduction_reliability), perfect durability does not exist: if all your
hard disks and all your backups are destroyed at the same time, there’s obviously nothing your
database can do to save you.