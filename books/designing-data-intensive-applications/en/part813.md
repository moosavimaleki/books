
Whenever a mapper finishes reading its input file and writing its sorted output files, the MapReduce
scheduler notifies the reducers that they can start fetching the output files from that mapper. The
reducers connect to each of the mappers and download the files of sorted key-value pairs for their
partition. The process of partitioning by reducer, sorting, and copying data partitions from mappers
to reducers is known as the shuffle [[26](ch10.html#White2015vl)] (a
confusing term—unlike shuffling a deck of cards, there is no randomness in MapReduce). 
The reduce task takes the files from the mappers and merges them together, preserving the sort
order. Thus, if different mappers produced records with the same key, they will be adjacent in the
merged reducer input. The reducer is called with a key and an iterator that incrementally scans over all records with the
same key (which may in some cases not all fit in memory). The reducer can use arbitrary logic to
process these records, and can generate any number of output records. These output records are
written to a file on the distributed filesystem (usually, one copy on the local disk of the machine
running the reducer, with replicas on other machines).