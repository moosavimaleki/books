Now we can make a simple change to the format of our segment files: we require that the sequence of
key-value pairs is sorted by key. At first glance, that requirement seems to break our ability to
use sequential writes, but we’ll get to that in a moment. 
We call this format Sorted String Table, or SSTable for short. We also require that each key
only appears once within each merged segment file (the compaction process already ensures that).
SSTables have several big advantages over log segments with hash indexes: 1.  
Merging segments is simple and efficient, even if the files are bigger than the available memory.
The approach is like the one used in the mergesort algorithm and is illustrated in
[Figure 3-4](#fig_storage_sstable_merging): you start reading the input files side by side, look at the first
key in each file, copy the lowest key (according to the sort order) to the output file, and repeat.
This produces a new merged segment file, also sorted by key.