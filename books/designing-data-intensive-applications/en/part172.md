Moreover, some operations require several different pages to be overwritten. For example, if you
split a page because an insertion caused it to be overfull, you need to write the two pages that
were split, and also overwrite their parent page to update the references to the two child pages.
This is a dangerous operation, because if the database crashes after only some of the pages have
been written, you end up with a corrupted index (e.g., there may be an orphan page that is not a
child of any parent). 
In order to make the database resilient to crashes, it is common for B-tree implementations to
include an additional data structure on disk: a write-ahead log (WAL, also known as a redo log).
This is an append-only file to which every B-tree modification must be written before it can be
applied to the pages of the tree itself. When the database comes back up after a crash, this log is
used to restore the B-tree back to a consistent state
[[5](ch03.html#Graefe2011kk),
[20](ch03.html#Mohan1992wo)].