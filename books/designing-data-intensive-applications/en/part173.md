An additional complication of updating pages in place is that careful concurrency control is
required if multiple threads are going to access the B-tree at the same time—otherwise a thread may
see the tree in an inconsistent state. This is typically done by protecting the tree’s data
structures with latches (lightweight locks). Log-structured approaches are simpler in this regard,
because they do all the merging in the background without interfering with incoming queries and
atomically swap old segments for new segments from time to time. ### B-tree optimizations 
As B-trees have been around for so long, it’s not surprising that many optimizations have been
developed over the years. To mention just a few: *  
Instead of overwriting pages and maintaining a WAL for crash recovery, some databases (like LMDB)
use a copy-on-write scheme [[21](ch03.html#Chu2014we)].
A modified page is written to a different location, and a new version of the parent pages in the tree
is created, pointing at the new location. This approach is also useful for concurrency control, as we shall
see in [“Snapshot Isolation and Repeatable Read”](ch07.html#sec_transactions_snapshot_isolation).