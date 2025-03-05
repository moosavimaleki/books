
Another approach is used in CouchDB, Datomic, and LMDB. Although they also use B-trees (see
[“B-Trees”](ch03.html#sec_storage_b_trees)), they use an append-only/copy-on-write variant that does not overwrite
pages of the tree when they are updated, but instead creates a new copy of each modified page.
Parent pages, up to the root of the tree, are copied and updated to point to the new versions of
their child pages.  Any pages that are not affected by a write do not need to be copied, and remain
immutable [[33](ch07.html#Prokopov2014uu),
[34](ch07.html#Schwartz2013ur_ch7),
[35](ch07.html#Anderson2010wj_ch7)]. With append-only B-trees, every write transaction (or batch of transactions) creates a new B-tree
root, and a particular root is a consistent snapshot of the database at the point in time when it
was created. There is no need to filter out objects based on transaction IDs because subsequent
writes cannot modify an existing B-tree; they can only create new tree roots. However, this approach also
requires a background process for compaction and garbage collection.