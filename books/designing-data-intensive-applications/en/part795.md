On the other hand, if the job’s working set is larger than the available memory, the sorting approach has the
advantage that it can make efficient use of disks. It’s the same principle as we discussed in
[“SSTables and LSM-Trees”](ch03.html#sec_storage_lsm_trees): chunks of data can be sorted in memory and written out to disk as segment
files, and then multiple sorted segments can be merged into a larger sorted file. Mergesort has
sequential access patterns that perform well on disks. (Remember that optimizing for sequential I/O
was a recurring theme in [Chapter 3](ch03.html#ch_storage). The same pattern reappears here.) 
The sort utility in GNU Coreutils (Linux) automatically handles larger-than-memory datasets by
spilling to disk, and automatically parallelizes sorting across multiple CPU cores
[[9](ch10.html#GNUCoreutils)].
This means that the simple chain of Unix commands we saw earlier easily scales to large datasets, without
running out of memory. The bottleneck is likely to be the rate at which the input file can be read
from disk.