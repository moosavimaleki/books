
As described so far, we only ever append to a file—so how do we avoid eventually running out of
disk space? A good solution is to break the log into segments of a certain size by closing a segment
file when it reaches a certain size, and making subsequent writes to a new segment file. We can then
perform compaction on these segments, as illustrated in [Figure 3-2](#fig_storage_compaction). Compaction
means throwing away duplicate keys in the log, and keeping only the most recent update for each key. ![ddia 0302](assets/ddia_0302.png) ###### Figure 3-2. Compaction of a key-value update log (counting the number of times each cat video was played), retaining only the most recent value for each key. 
Moreover, since compaction often makes segments much smaller (assuming that a key is overwritten
several times on average within one segment), we can also merge several segments together at the
same time as performing the compaction, as shown in [Figure 3-3](#fig_storage_merging). Segments are never
modified after they have been written, so the merged segment is written to a new file. The merging
and compaction of frozen segments can be done in a background thread, and while it is going on, we
can still continue to serve read and write requests as normal, using the old segment files. After
the merging process is complete, we switch read requests to using the new merged segment instead of
the old segments—and then the old segment files can simply be deleted.