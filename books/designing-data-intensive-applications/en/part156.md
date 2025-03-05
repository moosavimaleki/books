![ddia 0303](assets/ddia_0303.png) ###### Figure 3-3. Performing compaction and segment merging simultaneously. Each segment now has its own in-memory hash table, mapping keys to file offsets. In order to find
the value for a key, we first check the most recent segment’s hash map; if the key is not present we
check the second-most-recent segment, and so on. The merging process keeps the number of segments
small, so lookups don’t need to check many hash maps. Lots of detail goes into making this simple idea work in practice. Briefly, some of the
issues that are important in a real implementation are: File format CSV is not the best format for a log. It’s faster and simpler to use a binary format that first
encodes the length of a string in bytes, followed by the raw string (without need for escaping). Deleting records 
If you want to delete a key and its associated value, you have to append a special deletion record
to the data file (sometimes called a tombstone). When log segments are merged, the tombstone
tells the merging process to discard any previous values for the deleted key.