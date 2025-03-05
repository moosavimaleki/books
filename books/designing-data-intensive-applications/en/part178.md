### Downsides of LSM-trees 
A downside of log-structured storage is that the compaction process can sometimes interfere with the
performance of ongoing reads and writes. Even though storage engines try to perform compaction
incrementally and without affecting concurrent access, disks have limited resources, so it can
easily happen that a request needs to wait while the disk finishes an expensive compaction
operation. The impact on throughput and average response time is usually small, but at higher
percentiles (see [“Describing Performance”](ch01.html#sec_introduction_percentiles)) the response time of queries to log-structured
storage engines can sometimes be quite high, and B-trees can be more predictable
[[28](ch03.html#Mutsuzaki2011wx)]. 
Another issue with compaction arises at high write throughput: the disk’s finite write bandwidth
needs to be shared between the initial write (logging and flushing a
memtable to disk) and the
compaction threads running in the background. When writing to an empty database, the full disk
bandwidth can be used for the initial write, but the bigger the database gets, the more disk
bandwidth is required for compaction.