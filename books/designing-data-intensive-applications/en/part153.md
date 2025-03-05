## Hash Indexes 
Let’s start with indexes for key-value data. This is not the only kind of data you can index, but
it’s very common, and it’s a useful building block for more complex indexes. 
Key-value stores are quite similar to the dictionary type that you can find in most programming
languages, and which is usually implemented as a hash map (hash table). Hash maps are described in
many algorithms textbooks
[[1](ch03.html#Aho1983vj),
[2](ch03.html#Cormen2009uw)],
so we won’t go into detail of how they work here. Since we already have hash maps for our in-memory
data structures, why not use them to index our data on disk? Let’s say our data storage consists only of appending to a file, as in the preceding example. Then
the simplest possible indexing strategy is this: keep an in-memory hash map where every key is
mapped to a byte offset in the data file—the location at which the value can be found, as
illustrated in [Figure 3-1](#fig_storage_csv_hash_index). Whenever you append a new key-value pair to the file,
you also update the hash map to reflect the offset of the data you just wrote (this works both for
inserting new keys and for updating existing keys).  When you want to look up a value, use the hash
map to find the offset in the data file, seek to that location, and read the value.