### Performance optimizations 
As always, a lot of detail goes into making a storage engine perform well in practice. For example,
the LSM-tree algorithm can be slow when looking up keys that do not exist in the database: you have
to check the memtable, then the segments all the way back to the oldest (possibly having to read
from disk for each one) before you can be sure that the key does not exist. In order to optimize
this kind of access, storage engines often use additional Bloom filters
[[15](ch03.html#Bloom1970gl)].
(A Bloom filter is a memory-efficient data structure for approximating the contents of a set. It
can tell you if a key does not appear in the database, and thus saves many unnecessary disk reads
for nonexistent keys.) 
There are also different strategies to determine the order and timing of how SSTables are compacted
and merged. The most common options are size-tiered and leveled compaction. LevelDB and RocksDB
use leveled compaction (hence the name of LevelDB), HBase uses size-tiered, and Cassandra supports both
[[16](ch03.html#CassandraCompaction)]. In size-tiered
compaction, newer and smaller SSTables are successively merged into older and larger SSTables. In
leveled compaction, the key range is split up into smaller SSTables and older data is moved into
separate “levels,” which allows the compaction to proceed more incrementally and use less disk
space.