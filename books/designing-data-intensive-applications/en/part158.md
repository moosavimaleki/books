An append-only log seems wasteful at first glance: why don’t you update the file in place,
overwriting the old value with the new value? But an append-only design turns out to be good for
several reasons: *  
Appending and segment merging are sequential write operations, which are generally much faster
than random writes, especially on magnetic spinning-disk hard drives. To some extent sequential
writes are also preferable on flash-based solid state drives (SSDs)
[[4](ch03.html#Li2010te)]. We will discuss this issue further in [“Comparing B-Trees and LSM-Trees”](#sec_storage_btree_lsm_comparison). *  
Concurrency and crash recovery are much simpler if segment files are append-only or immutable. For
example, you don’t have to worry about the case where a crash happened while a value was being
overwritten, leaving you with a file containing part of the old and part of the new value spliced
together. *  Merging old segments avoids the problem of data files getting fragmented over time.