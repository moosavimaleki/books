## Comparing Hadoop to Distributed Databases 
As we have seen, Hadoop is somewhat like a distributed version of Unix, where HDFS is the
filesystem and MapReduce is a quirky implementation of a Unix process (which happens to always run
the sort utility between the map phase and the reduce phase). We saw how you can implement various
join and grouping operations on top of these primitives. 
When the MapReduce paper [[1](ch10.html#Dean2004ua_ch10)] was
published, it was—in some sense—not at all new. All of the processing and parallel join
algorithms that we discussed in the last few sections had already been implemented in so-called
massively parallel processing (MPP) databases more than a decade previously
[[3](ch10.html#Babu2013gm_ch10), [40](ch10.html#DeWitt1992ws)].
For example, the Gamma database machine, Teradata, and Tandem NonStop SQL were pioneers in this area
[[52](ch10.html#DeWitt1992fn_ch10)]. 
The biggest difference is that MPP databases focus on parallel execution of analytic SQL queries on
a cluster of machines, while the combination of MapReduce and a distributed filesystem
[[19](ch10.html#Ghemawat2003dy)] provides something much more like a
general-purpose operating system that can run arbitrary programs.