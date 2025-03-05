### Distributed execution of MapReduce 
The main difference from pipelines of Unix commands is that MapReduce can parallelize a computation
across many machines, without you having to write code to explicitly handle the parallelism. The
mapper and reducer only operate on one record at a time; they don’t need to know where their input
is coming from or their output is going to, so the framework can handle the complexities of moving
data between machines. 
It is possible to use standard Unix tools as mappers and reducers in a distributed computation
[[25](ch10.html#Gregg2013wz)], but more commonly they are implemented as
functions in a conventional programming language. In Hadoop MapReduce, the mapper and reducer are
each a Java class that implements a particular interface. In MongoDB and CouchDB, mappers and
reducers are JavaScript functions (see [“MapReduce Querying”](ch02.html#sec_datamodels_mapreduce)). [Figure 10-1](#fig_batch_mapreduce) shows the dataflow in a Hadoop MapReduce job. Its parallelization is based
on partitioning (see [Chapter 6](ch06.html#ch_partitioning)): the input to a job is typically a directory in HDFS, and
each file or file block within the input directory is considered to be a separate partition that can
be processed by a separate map task (marked by m 1, m 2, and m 3 in
[Figure 10-1](#fig_batch_mapreduce)).