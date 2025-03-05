
Maintaining a sorted structure on disk is possible (see [“B-Trees”](#sec_storage_b_trees)), but maintaining it
in memory is much easier. There are plenty of well-known tree data structures that you can use, such
as red-black trees or AVL trees [[2](ch03.html#Cormen2009uw)]. With
these data structures, you can insert keys in any order and read them back in sorted order. We can now make our storage engine work as follows: *  
When a write comes in, add it to an in-memory balanced tree data structure (for example, a
red-black tree). This in-memory tree is sometimes called a memtable. *  When the memtable gets bigger than some threshold—typically a few megabytes—write it out to
disk as an SSTable file. This can be done efficiently because the tree already maintains the
key-value pairs sorted by key. The new SSTable file becomes the most recent segment of the
database. While the SSTable is being written out to disk, writes can continue to a new memtable instance.