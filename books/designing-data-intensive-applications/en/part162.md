![ddia 0305](assets/ddia_0305.png) ###### Figure 3-5. An SSTable with an in-memory index. You still need an in-memory index to tell you the offsets for some of the keys, but it can be
sparse: one key for every few kilobytes of segment file is sufficient, because a few kilobytes can
be scanned very quickly.[i](ch03.html#idm140605778351696) 3.  Since read requests need to scan over several key-value pairs in the requested range anyway, it
is possible to group those records into a block and compress it before writing it to disk (indicated
by the shaded area in [Figure 3-5](#fig_storage_sstable_index)). Each entry of the sparse in-memory index then
points at the start of a compressed block. Besides saving disk space, compression also reduces the
I/O bandwidth use. ### Constructing and maintaining SSTables 
Fine so far—but how do you get your data to be sorted by key in the first place? Our incoming
writes can occur in any order.