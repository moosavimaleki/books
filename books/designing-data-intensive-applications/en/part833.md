As discussed, map-side joins also make more assumptions about the size, sorting, and partitioning of
their input datasets. Knowing about the physical layout of datasets in the distributed
filesystem becomes important when optimizing join strategies: it is not sufficient to just know the
encoding format and the name of the directory in which the data is stored; you must also know the number of
partitions and the keys by which the data is partitioned and sorted. 
In the Hadoop ecosystem, this kind of metadata about the partitioning of datasets is often
maintained in HCatalog and the Hive metastore [[37](ch10.html#Grover2015tl)]. ## The Output of Batch Workflows 
We have talked a lot about the various algorithms for implementing workflows of MapReduce jobs, but
we neglected an important question: what is the result of all of that processing, once it is done?
Why are we running all these jobs in the first place?