
As mentioned in [“Making an LSM-tree out of SSTables”](#sec_storage_lsm_usage), Lucene uses a SSTable-like structure for its term
dictionary. This structure requires a small in-memory index that tells queries at which offset in
the sorted file they need to look for a key. In LevelDB, this in-memory index is a sparse collection
of some of the keys, but in Lucene, the in-memory index is a finite state automaton over the
characters in the keys, similar to a trie
[[38](ch03.html#Heinz2002hh)].
This automaton can be transformed into a Levenshtein automaton, which supports efficient search
for words within a given edit distance
[[39](ch03.html#Schulz2002jt)]. Other fuzzy search techniques go in the direction of document classification and machine learning.
See an information retrieval textbook for more detail
[e.g., [40](ch03.html#Manning2008vf)]. ### Keeping everything in memory 
The data structures discussed so far in this chapter have all been answers to the limitations of
disks. Compared to main memory, disks are awkward to deal with. With both magnetic disks and SSDs,
data on disk needs to be laid out carefully if you want good performance on reads and writes.
However, we tolerate this awkwardness because disks have two significant advantages: they are
durable (their contents are not lost if the power is turned off), and they have a lower cost per
gigabyte than RAM.