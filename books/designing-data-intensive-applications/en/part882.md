We discussed several join algorithms for MapReduce, most of which are also internally used in MPP
databases and dataflow engines. They also provide a good illustration of how partitioned algorithms
work: Sort-merge joins Each of the inputs being joined goes through a mapper that extracts the join key. By partitioning,
sorting, and merging, all the records with the same key end up going to the same call of the
reducer. This function can then output the joined records. Broadcast hash joins One of the two join inputs is small, so it is not partitioned and it can be entirely loaded into a
hash table. Thus, you can start a mapper for each partition of the large join input, load the hash
table for the small input into each mapper, and then scan over the large input one record at a
time, querying the hash table for each record. Partitioned hash joins