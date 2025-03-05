
The Hadoop ecosystem includes both random-access OLTP databases such as HBase (see
[“SSTables and LSM-Trees”](ch03.html#sec_storage_lsm_trees)) and MPP-style analytic databases such as Impala
[[41](ch10.html#Kornacker2015uv_ch10)]. Neither HBase nor Impala uses
MapReduce, but both use HDFS for storage. They are very different approaches to accessing and
processing data, but they can nevertheless coexist and be integrated in the same system. ### Designing for frequent faults 
When comparing MapReduce to MPP databases, two more differences in design approach stand out: the
handling of faults and the use of memory and disk. Batch processes are less sensitive to faults
than online systems, because they do not immediately affect users if they fail and they can always
be run again. If a node crashes while a query is executing, most MPP databases abort the entire query, and
either let the user resubmit the query or automatically run it again
[[3](ch10.html#Babu2013gm_ch10)]. As queries normally run for a few
seconds or a few minutes at most, this way of handling errors is acceptable, since the cost of
retrying is not too great.  MPP databases also prefer to keep as much data as possible in memory
(e.g., using hash joins) to avoid the cost of reading from disk.