
Moreover, LSM-trees are typically able to sustain higher write throughput than B-trees, partly because they
sometimes have lower write amplification (although this depends on the storage engine configuration
and workload), and partly because they sequentially write compact SSTable files rather than having
to overwrite several pages in the tree
[[26](ch03.html#Callaghan2016wk)].
This difference is particularly important on magnetic hard drives, where sequential writes are much
faster than random writes. LSM-trees can be compressed better, and thus often produce smaller files on disk than B-trees.
B-tree storage engines leave some disk space unused due to fragmentation: when a page is split or
when a row cannot fit into an existing page, some space in a page remains unused. Since LSM-trees
are not page-oriented and periodically rewrite SSTables to remove fragmentation, they have lower
storage overheads, especially when using leveled compaction
[[27](ch03.html#Callaghan2016cm)]. On many SSDs, the firmware internally uses a log-structured algorithm to turn random writes into
sequential writes on the underlying storage chips, so the impact of the storage engine’s write
pattern is less pronounced [[19](ch03.html#Goossaert2014wj)]. However,
lower write amplification and reduced fragmentation are still advantageous on SSDs: representing
data more compactly allows more read and write requests within the available I/O bandwidth.