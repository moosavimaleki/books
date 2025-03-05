![ddia 0304](assets/ddia_0304.png) ###### Figure 3-4. Merging several SSTable segments, retaining only the most recent value for each key. What if the same key appears in several input segments? Remember that each segment contains all the
values written to the database during some period of time. This means that all the values in one
input segment must be more recent than all the values in the other segment (assuming that we always
merge adjacent segments). When multiple segments contain the same key, we can keep the value from
the most recent segment and discard the values in older segments. 2.  
In order to find a particular key in the file, you no longer need to keep an index of all the
keys in memory. See [Figure 3-5](#fig_storage_sstable_index) for an example: say you’re looking for the key
handiwork, but you don’t know the exact offset of that key in the segment file. However, you do
know the offsets for the keys handbag and handsome, and because of the sorting you know that
handiwork must appear between those two. This means you can jump to the offset for handbag and scan from
there until you find handiwork (or not, if the key is not present in the file).