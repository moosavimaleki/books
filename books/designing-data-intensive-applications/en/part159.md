However, the hash table index also has limitations: *  The hash table must fit in memory, so if you have a very large number of keys, you’re out of luck.
In principle, you could maintain a hash map on disk, but unfortunately it is difficult to make an
on-disk hash map perform well. It requires a lot of random access I/O, it is expensive to grow
when it becomes full, and hash collisions require fiddly logic
[[5](ch03.html#Graefe2011kk)]. *  Range queries are not efficient. For example, you cannot easily scan over all keys
between kitty00000 and kitty99999—you’d have to look up each key individually in the hash
maps. In the next section we will look at an indexing structure that doesn’t have those limitations. ## SSTables and LSM-Trees 
In [Figure 3-3](#fig_storage_merging), each log-structured storage segment is a sequence of key-value pairs.
These pairs appear in the order that they were written, and values later in the log take precedence
over values for the same key earlier in the log. Apart from that, the order of key-value pairs in
the file does not matter.