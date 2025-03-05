Like SSTables, B-trees keep key-value pairs sorted by key, which allows efficient key-value lookups
and range queries. But that’s where the similarity ends: B-trees have a very different design
philosophy. The log-structured indexes we saw earlier break the database down into variable-size segments,
typically several megabytes or more in size, and always write a segment sequentially. By contrast,
B-trees break the database down into fixed-size blocks or pages, traditionally 4 KB in size
(sometimes  bigger), and read or write one page at a time. This design corresponds more closely to
the underlying hardware, as disks are also arranged in fixed-size blocks. Each page can be identified using an address or location, which allows one page to refer to
another—similar to a pointer, but on disk instead of in memory. We can use these page references to
construct a tree of pages, as illustrated in [Figure 3-6](#fig_storage_b_tree). ![ddia 0306](assets/ddia_0306.png) ###### Figure 3-6. Looking up a key using a B-tree index.