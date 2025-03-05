### Advantages of LSM-trees A B-tree index must write every piece of data at least twice: once to the write-ahead log, and once
to the tree page itself (and perhaps again as pages are split). There is also overhead from having
to write an entire page at a time, even if only a few bytes in that page changed. Some storage
engines even overwrite the same page twice in order to avoid ending up with a partially updated
page in the event of a power failure [[24](ch03.html#Zaitsev2006wa), [25](ch03.html#Vondra2016bp)]. 
Log-structured indexes also rewrite data multiple times due to repeated compaction and merging of
SSTables. This effect—one write to the database resulting in multiple writes to the disk over the
course of the database’s lifetime—is known as write amplification. It is of particular concern
on SSDs, which can only overwrite blocks a limited number of times before wearing out. In write-heavy applications, the performance bottleneck might be the rate at which the database can
write to disk. In this case, write amplification has a direct performance cost: the more that a
storage engine writes to disk, the fewer writes per second it can handle within the available disk
bandwidth.