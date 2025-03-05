
A much better solution is to build a brand-new database inside the batch job and write it as
files to the job’s output directory in the distributed filesystem, just like the search indexes in
the last section. Those data files are then immutable once written, and can be loaded in bulk into
servers that handle read-only queries. Various key-value stores support building database files in
MapReduce jobs, including Voldemort
[[46](ch10.html#Sumbaly2012wi)],
Terrapin [[47](ch10.html#Sharma2015tp)],
ElephantDB [[48](ch10.html#ElephantDB)],
and HBase bulk loading [[49](ch10.html#Cryans2013wo)]. Building these database files is a good use of MapReduce: using a mapper to extract a key and then
sorting by that key is already a lot of the work required to build an index. Since most of these
key-value stores are read-only (the files can only be written once by a batch job and are then
immutable), the data structures are quite simple. For example, they do not require a WAL (see
[“Making B-trees reliable”](ch03.html#sec_storage_btree_wal)).